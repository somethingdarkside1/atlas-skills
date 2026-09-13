---
part: plan-skill
date: 2026-09-13
status: accepted
---

# A task id is part/NN with files and the issue number with GitHub, everywhere

Tasks were numbered inside their part, so two parts could both hold a task 01 and `/build-it 01`, `Next: /build-it 01`, and `build 01:` were ambiguous. The id is now `<part>/<NN>` in files mode and the issue number in GitHub mode, in every place a skill prints or accepts one; only `blocked_by` inside a part may shorten it to `NN`, because the part is already known there.

Considered: a global counter across parts (breaks the flat per-part folder and re-plans); the number alone with the part inferred from context (the ambiguity that started this).
Revisit when: a tracker other than files or GitHub arrives with its own id shape.
