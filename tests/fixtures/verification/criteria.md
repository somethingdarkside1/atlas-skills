# Fixture criteria

Synthetic acceptance criteria for two deliveries. They are the source of truth for the checks.

## Late fee (code)

`late_fee(days_late)` in `late_fee.py` returns a fee in cents.

1. Up to 3 days late, the fee is 0.
2. From the 4th day late, the fee is 25 cents for each day beyond the third: 4 days late is 25, and 10 days late is 175.
3. The fee never exceeds 500 cents.
4. A negative number of days is an error (`ValueError`).

## Opening hours page (document)

`page.html` is delivered for the library website. `hours.csv` is the source of record for opening times.

1. Every day and time on the page matches `hours.csv`.
2. The holiday notice appears above the hours table.
3. The notice text has a contrast ratio of at least 4.5 to 1 against its background.
4. The page reads without sideways scrolling on a phone screen 375 pixels wide.
5. A first-time visitor notices the holiday notice.
