# Verification

Use when an output needs evidence that it meets its acceptance criteria: a builder checking its own result before recording delivery, or a reviewer checking a delivery it did not make. Choose checks from the output, its risks, and its criteria. Send an unexplained failure to the diagnosis method.

## Inputs

Identify the exact output, the criteria and scope it answers to, your role (builder or reviewer), the risks that would matter most if it were wrong, and the checks the project requires, which still run. Name where each criterion's expected answer comes from, such as the task, a source of record, a worked example, or a person.

## Process

1. Fix the identity. Follow the caller's evidence format to identify the actual output and applicable scope, including working changes. Use the project's versioning or its bundled evidence helper for files. For an external result, use a stable record/version and inspection time, or state why it cannot be retrieved. A checksum detects change but cannot restore old content; retain earlier accepted evidence when existing storage cannot recover it. Results taken before a change describe the earlier identity. Done when the next step can identify what was checked and under which criteria.
2. Choose checks that could fail. For each criterion and main risk, name an observation that would differ if the output were wrong, with expected values from that named source. A test that recomputes the answer the way the output does, or a description that restates the output, still passes when the output is wrong. Where cheap, show a new check failing on a known wrong version in a scratch copy. Check the criteria and project conventions separately, so a pass on one cannot hide a failure on the other. By medium:
   - Code: use the public interface, with positive cases and the relevant failure cases, such as boundaries, invalid input, and the reported defect.
   - Document: check each factual claim against its named source. Check a visual or layout claim by rendering at the stated sizes; reading the structure (element order, declared colors) is weaker, and the record says so.
   - Data, a process, or a setting: reconcile against the source of record, or inspect the actual state.

   Done when each criterion has a check, a stated reason no check is available, or a named human judgment.
3. Run and record. For each check, record what was run, what was seen (exit code, counts, the lines that matter), and what that observation cannot show. Give each check one outcome: passed, failed, not run with the reason, or human-only judgment. Report a pass only after seeing it. Done when every chosen check has an outcome and its evidence.
4. Keep the kinds of evidence apart. Builder verification is the builder's evidence about its own output. Independent review derives checks from the criteria, in a separate context when available, and reruns them instead of trusting the builder's report. A platform status, such as a CI result or a PR approval, shows only what that platform ran or recorded; quote it as reported, and never count it as builder verification or review. Done when the record names its role and claims no more than it has.

## Return to the caller

Return a compact record containing:

- Identity: the revision, the checksum line with its file list, or what was looked at and when; the role; and the environment when it matters.
- Checks: for each, the criterion, what was run, what was seen, the outcome, and its limit.
- Open items: failed checks, checks not run with the reason, and human-only judgments with what to look at.
- Platform status: any CI result or PR approval, quoted as reported.

Keep only evidence the next step uses, without secrets. The caller selects the durable home and owns task state, acceptance, and project delivery.

## Attribution

Adapted from Matt Pocock's [tdd](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md) and [code-review](https://github.com/mattpocock/skills/blob/main/skills/engineering/code-review/SKILL.md), inspected from the local reference labeled 1.2.3. They inspired tests through public interfaces, expected values from an independent source, a fixed review target, and reviewing what was asked separately from coding standards. Atlas adds identity without Git, non-code checks, checks not run, and keeping builder checks, review, and platform status apart. The URLs are locators, not pinned revisions; the [task evidence](https://github.com/somethingdarkside1/atlas-skills/blob/72e890a/notes/2026-09-17-review-verification-and-prototype-methods.md) identifies the inspected files.

MIT License

Copyright (c) 2026 Matt Pocock

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
