# OBSERVATIONS-Form — der Instrument-Lektions-Träger (Vorlage)

Rolle: prozess-/werkzeugbezogene Schwächen, die im BETRIEB einer
Session auffallen, landen im Repo des BESITZENDEN Instruments —
Dispatch-Lektionen hier (`dispatch-OBSERVATIONS.md`), abw-Lektionen in
pbs-abwaegung, Büro-Prozess im pbs-office-Backlog, Arbeits-Ethik (in
jedem Projekt wahr) im Operator-Korpus. Nie ein globaler Pool: die eine
Sammelliste, die jede Session verlängert und niemand leert, ist der
gemessene Fehlschlag, den diese Form ersetzt (beobachtet
vendor/claude-code-cache-fix: Auto-Buchung ohne Konsument, ohne
Gradierung, ohne Dedup, ohne Abfluss-Trigger — inhaltlich richtige
Einträge, funktional Müllhalde).

## Eintrags-Form (vier Pflicht-Slots)

1. **Vorfall + Basis** — was geschah, mit Fundstelle (Session/Journal/
   Commit); Häufigkeit, wenn > 1.
2. **Klasse** — die Fehlerklasse, nicht das Symptom. GLEICHE KLASSE =
   MERGE in den bestehenden Eintrag (Zähler hoch, Fundstelle dazu),
   nie ein Geschwister-Eintrag.
3. **Vorformulierter Regel-/Fix-Text** — der Wortlaut, den der
   Wartungs-Pass anwenden würde. Dieser Slot macht den Pass zum
   mechanischen Anwenden+Prüfen statt zur Neu-Herleitung; ein Eintrag
   ohne ihn ist eine halbe Buchung.
4. **Konsument + Abfluss-Naht** — welcher Pass/welche Runde den
   Eintrag anwendet (z. B. „nächste dispatch-guards-Maintenance-Runde",
   „nächster Bau am Wächter X").

## Abfluss (Quote, nie Kalender)

Der Träger schuldet einen Wartungs-Pass, wenn Buchungen seit dem
letzten Pass Anwenden+Verwerfen deutlich überholen (Faustgröße 3:1 —
dieselbe Quote wie der Backlog-Retirement-Trigger im Operator-Korpus).
Der Pass wendet den vorformulierten Text an ODER verwirft mit
Ein-Zeilen-Begründung — beides ist ein Abgang, die Liste schrumpft.
Angewandte/verworfene Einträge wandern in einen `## Abgeflossen`-
Abschnitt mit Beleg (Commit/Begründung) — ein Fakt, eine Heimat.

## Erfassungs-Naht

Das Sitzungsende trägt eine Präsenz-Zeile („Ernte: <Buchungen mit
Heimat>" oder „Ernte: keine") — die fehlende Zeile ist sichtbar, das
Urteil selbst bleibt Urteil. Site-Instanz: pbs-office RUNBOOK R13
Schritt 3; Korpus-Rolle: Operator-CLAUDE.md, Accretion-Modul.
