# Prototype cases

Copy this directory into a scratch folder at the same path, `tests/fixtures/prototype/`, before running or changing it. These synthetic cases exercise [the prototype method](../../../methods/prototype.md) on three kinds of question. They are not production code or an automated test of agent reasoning. Each prototype states its question, kind, and bound at the top.

Logic behavior: [holds.py](holds.py) asks whether a proposed hold rule can leave a book on the shelf while a member waits. Run `python3 holds.py` for the proposed rule and `python3 holds.py pass-on` for the alternative. Each run prints three walkthroughs with the state after every action, then checks every legal sequence of up to six actions. That check is part of the prototype because the question is about every sequence, not one example.

UI preference: open [options.html](options.html) in a browser to compare a one-screen renewal form with a two-step form. Run `python3 measure_options.py` for counts of fields, buttons, steps, and words. The counts inform the choice; the preference belongs to a person.

Other media: [subjects.md](subjects.md) holds two email subject lines. Read them, and measure their lengths with `python3 -c "import re; [print(len(m[2]), m[1]) for m in re.finditer(r'^([AB]): (.+)$', open('subjects.md').read(), re.M)]"`. The deciding evidence is how real members respond, which this folder does not contain. The method still drafts the options and measures what it can, then returns `not clear yet` with the next experiment and what it needs.

None of these cases needs saved data. The [evidence note](../../../notes/2026-09-17-review-verification-and-prototype-methods.md) records what was run and what was seen.
