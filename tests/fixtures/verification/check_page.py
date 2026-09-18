"""Check page.html against criteria 1 to 3 in criteria.md.

This reads the page source. It does not render the page, so it cannot show
phone layout (criterion 4) or whether a person notices the notice (criterion 5).
"""
import csv
import re
import sys
from html.parser import HTMLParser


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.order, self.rows, self.row, self.cell, self.style = [], [], None, None, ""
        self.in_style = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "style":
            self.in_style = True
        if "notice" in (attrs.get("class") or "").split():
            self.order.append("notice")
        if tag == "table":
            self.order.append("table")
        if tag == "tr":
            self.row = []
        if tag == "td":
            self.cell = ""

    def handle_endtag(self, tag):
        if tag == "style":
            self.in_style = False
        if tag == "td":
            self.row.append(self.cell.strip())
            self.cell = None
        if tag == "tr" and self.row:
            self.rows.append(self.row)

    def handle_data(self, data):
        if self.in_style:
            self.style += data
        if self.cell is not None:
            self.cell += data


def luminance(hex_color):
    channels = [int(hex_color[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    r, g, b = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


page = Page()
page.feed(open("page.html").read())
failures = 0

with open("hours.csv", newline="") as source:
    expected = {row["day"]: [row["opens"], row["closes"]] for row in csv.DictReader(source)}
shown = {}
for row in page.rows:
    shown.setdefault(row[0], []).append(row[1:])
for day in expected:
    # Exactly one row per day, so a repeated day fails even if one copy is right.
    passed = shown.get(day) == [expected[day]]
    failures += not passed
    print(f"criterion 1: {day} source={expected[day]} page rows={shown.get(day, [])} {'pass' if passed else 'fail'}")
extra = sorted(set(shown) - set(expected))
failures += bool(extra)
print(f"criterion 1: days on page but not in source={extra} {'fail' if extra else 'pass'}")

passed = "notice" in page.order and "table" in page.order and page.order.index("notice") < page.order.index("table")
failures += not passed
print(f"criterion 2: source order={page.order} {'pass' if passed else 'fail'}")

rule = re.search(r"\.notice\s*\{([^}]*)\}", page.style)
rule = rule[1] if rule else ""
foreground = re.search(r"(?<![-\w])color:\s*(#[0-9a-fA-F]{6})\b", rule)
background = re.search(r"(?<![-\w])background(?:-color)?:\s*(#[0-9a-fA-F]{6})\b", rule)
if foreground and background:
    light, dark = sorted([luminance(foreground[1]), luminance(background[1])], reverse=True)
    ratio = (light + 0.05) / (dark + 0.05)
    passed = ratio >= 4.5
    print(f"criterion 3: declared {foreground[1]} on {background[1]} ratio={ratio:.2f} {'pass' if passed else 'fail'}")
else:
    passed = False
    print(f"criterion 3: notice colors missing or unreadable in the .notice rule: {rule.strip() or 'no rule'} fail")
failures += not passed

sys.exit(1 if failures else 0)
