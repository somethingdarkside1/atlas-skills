---
date: 2026-09-17
kind: research
part: core-model
---

# How much evidence a task should carry

## Summary
Evidence earns its place when the next skill uses it, and most of the heavy record this repository writes is read by nobody. The recommended default is two short lines: a `Version:` checksum of the delivered files on each Delivered entry, and a matching `Reviewed:` line on each Review pass, beside a Delivered that says what was run and what was seen. This is analysis without run data; the first real runs of 0.2 should confirm which failures actually happen before [core-model/02](../plan/core-model/02-define-task-evidence.md) fixes the fields.

## Detail

### What evidence is for

Six things can make a "done" untrue. They differ a great deal in how often they happen to one person working with an agent.

| # | Failure | How it happens | How likely | What actually stops it |
|---|---|---|---|---|
| 1 | Wrong target | The files change between delivery and review, or review runs in another checkout | Medium with worktrees, low in a plain folder | Knowing exactly what was delivered |
| 2 | Rework confusion | Findings, a second delivery, then "clean": which one? | Every task with findings | Dated Delivered entries and dated passes |
| 3 | False "verified" | Delivered says a check passed that did not run or did not pass | The most common agent failure | Saying what was run and what was seen; the reviewer running Check by again |
| 4 | Scope moved | The brief changes after the review | Whenever a building part is re-interviewed | The interview naming the tasks it touches |
| 5 | Later change | Someone edits the thing after done | Normal, and fine | Git history; nothing light without git |
| 6 | Missing base | A task starts on a blocker whose output is elsewhere | Only with a branch per task | The project's own saving rule |

The 0.2 patch already covers 2 and 4: Delivered and Review are dated entries, there is a `review` status, and `/interview-me` names the tasks a changed brief touches. It leans on the reviewer re-running Check by for 3. It does nothing for 1.

### The options

| Option | What a task carries | Words per task | Covers | Weakness |
|---|---|---|---|---|
| A. As 0.2 | Dated entries, statuses | about 40 | 2, 4, part of 3 | Nothing for 1 |
| B. One line each side | A, plus `Version:` and `Reviewed:` | about 60 | 1, 2, 4, part of 3 | Identifies the files; does not keep a copy |
| C. Full record | Start, output, and scope revisions, a criteria table, limits, checker output | 547 and 528 in this repository's two done tasks | 1, 2, 4 on paper | Nobody reads it, no skill uses most of it, and more claims mean more places for a false one |
| D. Git history only | Nothing; the commits are the record | 0 | 1, 2 in a repo | Breaks when a project squashes or batches commits, which decision 0012 allows; nothing without git |
| E. Snapshots | A copy of the delivered files beside the task | files | 1, 2, 5 | Doubles the files; clutter |

### What is most effective

Follow each field to the skill that uses it. `/review-it` uses the file list, the version, and how the builder checked. `/build-it` uses findings that say what, where, and how to fix. `/atlas` uses the status and whether Delivered is filled. No skill uses a start revision, a scope revision, a limits paragraph, or a table that restates the Done when boxes; the ticks are already the record per criterion. Fields with no reader turn into ritual, and ritual text is itself a set of unchecked claims ("no unrelated edits were present").

So the default should be option B, with Delivered sharpened against failure 3:

```md
## Delivered
### 2026-09-17
Made: horizontal and stacked lockups in `wordmark/lockups.svg`, shown in `wordmark/lockups.html`.
Checked: opened lockups.html at 16, 64, and 400 pixels; both lockups draw; clear space is 1.5 x-heights in both.
Not checked: whether they read cleanly at 16 pixels (yours).
Version: 3f9a1c2e7b04 (2 files)

## Review
### 2026-09-17
Reviewed: 3f9a1c2e7b04
Brief: clean.
Conventions: lockups.html line 12 says "padding"; the glossary says clear space. Replace the word.
```

- `Version:` is a checksum over the files named under Made, shortened to twelve characters. One command, the same with or without git, and it avoids the trap of a commit hash, which cannot sit inside the commit it names. A delivery that is not a file (a sent email, a setting in a CRM) writes what to look at and the date instead.
- `/review-it` recomputes it first. Equal: review, and write `Reviewed:`. Different: say which files changed since delivery and hand back to `/build-it`, because the builder's checks no longer describe the thing.
- The person never computes or reads a checksum. They see two short lines.
- A project that needs more (this repository, regulated work, several agents) says so in its own instructions, the same way it owns its saving rule. Option C stays available; it stops being the default.

### Where this meets decision 0019

[0019](../decisions/0019-acceptance-follows-output-and-scope.md) asks for "a preserved version or snapshot with content identity" outside git. Option B gives the identity and not the preserved copy: it can tell that a file changed, and cannot bring back the reviewed one. Full compliance without git means option E. The proposal is to narrow 0019: identity by default, a kept copy only when the project asks for it or the thing leaves the building (a signed-off PDF). That is Vitali's call and needs a superseding decision if taken.

### Limits

The likelihoods above are judgment, not counts. The cheap test is the first ten real tasks under 0.2: note each time one of the six failures happens. If failure 1 never shows up, even the `Version:` line is more than the default needs. The 0.2 patch ships without it for that reason.

## Copied into
Nothing durable. Input to [core-model/02](../plan/core-model/02-define-task-evidence.md), which owns the fields.
