#!/usr/bin/env python3
"""Lane-cost miner: what a fan-out actually cost, from its own transcripts.

Answers the sizing question §1 leaves open for READ-ONLY fan-outs,
where no write-boundary join exists to derive lanes from: is splitting
work across N lanes token-cheaper than running it in one, and above
how many tool calls per lane does splitting start paying?

The mechanism, since the answer is counter-intuitive: a single lane
re-reads its whole accumulated prefix on every call, so its read cost
grows QUADRATICALLY in call count, while splitting pays a fixed
per-lane startup once. Past a crossover the quadratic term dominates
and splitting is cheaper on tokens alone — the opposite of the folk
intuition that more agents cost more.

    n* = sqrt(4 * C_lane / (w_r * g))

where C_lane is the weighted marginal cost of one more lane, g the
per-call context growth, w_r the cache-read price weight. Carry the
FORMULA; g and C_lane are workload-specific and this script measures
them from real transcripts rather than assuming them.

THE CONSTANT THIS SCRIPT EXISTS TO GET RIGHT: g is per-call GROWTH, so
it is derived from calls 2..n only. Dividing total cache-creation by
total calls folds each lane's one-time startup into the growth term
and inflates it — measured 1.56x on the first real fan-out this was
run against, which moved the modeled ratio from 3.7x to 2.6x and the
crossover from 23 calls to 29. A sizing rule of thumb is exactly the
consumer that difference reaches, so the split is computed here and
both figures printed, never one.

Usage:  lane-cost.py <transcript.jsonl> [...]      (shell-globbed)
        lane-cost.py --test

Provenance: mined from a 5-lane read-only fan-out, 2026-08-15; the
measurement half is real per-request usage, the single-lane arm is
MODELED from measured growth and has never been run. Graduated to
tools/ under the probe-used-twice rule.
"""
from __future__ import annotations

import collections
import json
import sys

# Price weights relative to a fresh input token. ASSUMED, not verified
# against billing — raw counts are the measurement, weighted figures
# are an overlay. Both are printed so a reader can discount the
# overlay without losing the measurement.
W_READ = 0.1
W_CREATE = 1.25


def lane_usage(path: str) -> dict | None:
    """Per-request usage for one transcript, deduped by requestId.

    LAST snapshot per requestId wins: transcript usage entries are
    per-stream snapshots of the same API call, so summing them raw
    multiply-counts a single request (corpus: dedupe by API-call id
    before summing)."""
    reqs: collections.OrderedDict = collections.OrderedDict()
    try:
        fh = open(path, encoding="utf-8", errors="replace")
    except OSError:
        return None
    with fh:
        for line in fh:
            try:
                o = json.loads(line)
            except (json.JSONDecodeError, ValueError):
                continue
            u = (o.get("message") or {}).get("usage")
            if u:
                reqs[o.get("requestId")] = u
    vals = list(reqs.values())
    if not vals:
        return None
    n = lambda v, k: v.get(k, 0) or 0            # noqa: E731
    first = vals[0]
    return {
        "calls": len(vals),
        "first_create": n(first, "cache_creation_input_tokens"),
        "first_read": n(first, "cache_read_input_tokens"),
        "first_load": (n(first, "cache_creation_input_tokens")
                       + n(first, "cache_read_input_tokens")
                       + n(first, "input_tokens")),
        "creation": sum(n(v, "cache_creation_input_tokens") for v in vals),
        "read": sum(n(v, "cache_read_input_tokens") for v in vals),
        "out": sum(n(v, "output_tokens") for v in vals),
    }


def analyse(lanes: dict[str, dict]) -> dict:
    """Measured totals plus the modeled single-lane counterfactual.

    Returns BOTH growth constants — the naive one (total creation over
    total calls) and the corrected one (growth calls only) — because
    the naive one is the trap this tool documents, and a reader who
    sees only the corrected number cannot tell the tool avoided it."""
    calls = sum(l["calls"] for l in lanes.values())
    creation = sum(l["creation"] for l in lanes.values())
    read = sum(l["read"] for l in lanes.values())
    startup = sum(l["first_create"] for l in lanes.values())
    n_lanes = len(lanes)
    growth_calls = calls - n_lanes
    g_naive = creation / calls if calls else 0.0
    g = (creation - startup) / growth_calls if growth_calls > 0 else 0.0
    # Arrival context: the first lane's first-call load (the full
    # prefix, nothing yet cached to read).
    arrival = max(l["first_load"] for l in lanes.values())
    # One lane, same total calls, one prefix growing by g per call.
    modeled = calls * arrival + g * (calls * (calls - 1) // 2)
    marginal = min(
        (l["first_create"] for l in lanes.values()), default=0)
    marginal_read = min(
        (l["first_read"] for l in lanes.values()), default=0)
    c_lane = marginal * W_CREATE + marginal_read * W_READ
    n_star = (4 * c_lane / (W_READ * g)) ** 0.5 if g > 0 else float("inf")
    return {
        "lanes": n_lanes, "calls": calls, "creation": creation,
        "read": read, "startup": startup, "arrival": arrival,
        "g_naive": g_naive, "g": g, "inflation": (g_naive / g) if g else 0.0,
        "modeled_read": modeled,
        "ratio_raw": (modeled / read) if read else 0.0,
        "c_lane": c_lane, "n_star": n_star,
    }


def report(lanes: dict[str, dict], a: dict) -> str:
    out = [f"{'lane':<10}{'calls':>7}{'1st-load':>10}{'1st-create':>12}"
           f"{'creation':>11}{'read':>13}"]
    for name, l in lanes.items():
        out.append(f"{name:<10}{l['calls']:>7}{l['first_load']:>10,}"
                   f"{l['first_create']:>12,}{l['creation']:>11,}"
                   f"{l['read']:>13,}")
    out.append(f"{'TOTAL':<10}{a['calls']:>7}{'':>10}{a['startup']:>12,}"
               f"{a['creation']:>11,}{a['read']:>13,}")
    out.append("")
    out.append(f"per-call growth g          : {a['g']:,.0f}"
               f"   (naive creation/calls would say {a['g_naive']:,.0f}"
               f" — inflated {a['inflation']:.2f}x by folding in the"
               f" one-time per-lane startup)")
    out.append(f"marginal lane C_lane       : {a['c_lane']:,.0f} weighted")
    out.append(f"measured read, {a['lanes']} lanes    : "
               f"{a['read']/1e6:,.2f}M")
    out.append(f"MODELED read, 1 lane       : {a['modeled_read']/1e6:,.2f}M"
               f"   (never run — modeled from measured g)")
    out.append(f"ratio (raw tokens)         : {a['ratio_raw']:.2f}x"
               f"   {'splitting cheaper' if a['ratio_raw'] > 1 else 'one lane cheaper'}")
    out.append(f"crossover n*               : {a['n_star']:,.0f} tool calls"
               f" per lane before splitting pays on tokens alone")
    return "\n".join(out)


def _test() -> int:
    """Synthetic fixture with known values; the assertion that matters
    is that g EXCLUDES per-lane startup."""
    import os
    import tempfile
    # 2 lanes x 3 calls. Startup 100 each; growth 10 per later call.
    def rec(rid, create, read):
        return json.dumps({"requestId": rid, "message": {"usage": {
            "cache_creation_input_tokens": create,
            "cache_read_input_tokens": read,
            "input_tokens": 0, "output_tokens": 5}}})
    with tempfile.TemporaryDirectory() as td:
        paths = []
        for lane in ("a", "b"):
            p = os.path.join(td, f"agent-{lane}.jsonl")
            with open(p, "w", encoding="utf-8") as f:
                f.write(rec(f"{lane}1", 100, 0) + "\n")
                # duplicate snapshot of the SAME request: must not
                # double-count (the per-stream-snapshot caveat)
                f.write(rec(f"{lane}1", 100, 0) + "\n")
                f.write(rec(f"{lane}2", 10, 100) + "\n")
                f.write(rec(f"{lane}3", 10, 110) + "\n")
            paths.append(p)
        lanes = {os.path.basename(p): lane_usage(p) for p in paths}
        assert all(v for v in lanes.values())
        assert lanes[os.path.basename(paths[0])]["calls"] == 3, "dedupe failed"
        a = analyse(lanes)
        assert a["calls"] == 6 and a["lanes"] == 2
        assert a["creation"] == 240, a["creation"]      # 2*(100+10+10)
        assert a["startup"] == 200, a["startup"]
        # the whole point: g is growth-only
        assert a["g"] == 10, a["g"]                      # 40/4
        assert abs(a["g_naive"] - 40) < 1e-9, a["g_naive"]   # 240/6
        assert abs(a["inflation"] - 4.0) < 1e-9
        # a run with no growth calls must not divide by zero
        one = {"x": {"calls": 1, "first_create": 100, "first_read": 0,
                     "first_load": 100, "creation": 100, "read": 0,
                     "out": 0}}
        b = analyse(one)
        assert b["g"] == 0 and b["n_star"] == float("inf")
        assert "inflated" in report(lanes, a)
    print("lane-cost: all tests passed")
    return 0


def main(argv: list[str]) -> int:
    if "--test" in argv:
        return _test()
    paths = [a for a in argv[1:] if not a.startswith("-")]
    if not paths:
        print(__doc__.strip().split("Usage:")[1].strip(), file=sys.stderr)
        return 2
    lanes = {}
    for p in paths:
        u = lane_usage(p)
        if u:
            lanes[p.rsplit("/", 1)[-1][:28]] = u
    if not lanes:
        print("no usable transcripts (no usage records found)",
              file=sys.stderr)
        return 2
    print(report(lanes, analyse(lanes)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
