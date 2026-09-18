"""PROTOTYPE helper. Count facts about each option in options.html.

These counts describe the drafts, leaving out each option's own heading.
They do not say which option a person prefers or which one members finish faster.
"""
from html.parser import HTMLParser


class Options(HTMLParser):
    def __init__(self):
        super().__init__()
        self.option, self.counts, self.labels, self.in_heading = None, {}, {}, False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "section" and attrs.get("id", "").startswith("option-"):
            self.option = attrs["id"]
            self.counts[self.option] = dict(fields=0, fields_before_first_button=0, buttons=0,
                                            steps=0, words_before_first_button=0, inputs=[])
            self.labels[self.option] = set()
        if self.option is None:
            return
        self.in_heading = tag == "h2"
        c = self.counts[self.option]
        if tag == "input":
            c["fields"] += 1
            c["inputs"].append(attrs.get("id"))
            if c["buttons"] == 0:
                c["fields_before_first_button"] += 1
        if tag == "label":
            self.labels[self.option].add(attrs.get("for"))
        if tag == "button":
            c["buttons"] += 1
        if tag == "div" and "step" in attrs.get("class", "").split():
            c["steps"] += 1

    def handle_endtag(self, tag):
        if tag == "section":
            self.option = None
        if tag == "h2":
            self.in_heading = False

    def handle_data(self, data):
        if self.option and not self.in_heading and self.counts[self.option]["buttons"] == 0:
            self.counts[self.option]["words_before_first_button"] += len(data.split())


parser = Options()
parser.feed(open("options.html").read())
for option, c in parser.counts.items():
    unlabeled = [i for i in c.pop("inputs") if i not in parser.labels[option]]
    c["steps"] = c["steps"] or 1
    print(f"{option}: " + ", ".join(f"{k}={v}" for k, v in c.items()) + f", fields_without_label={len(unlabeled)}")
