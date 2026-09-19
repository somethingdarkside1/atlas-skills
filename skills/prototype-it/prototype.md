<!-- Generated from methods/prototype.md; sha256=be38b15b77002bc54bcbea07142388babf9a2a4cd3670a481a0124c58e4a4ba1. Edit the source and regenerate. -->

# Prototype

Use when a choice depends on a question that reading or discussion cannot settle, and a small made thing could help answer it. When an accessible fact answers the question, look it up instead. When the deciding evidence is out of reach, such as how real customers respond, still draft the contrasting options and return `not clear yet` with the next experiment and what it needs. A prototype is not production work; what it teaches is the result.

## Inputs

Identify the question in one sentence, the decision it informs, who judges the answer, and a bound (one sitting unless the person said otherwise). Gather the real material the answer depends on, such as the module, page, data, or audience.

## Process

1. Frame the experiment. Write the question and the observation that would support each likely answer. Name its kind: a behavior the agent can measure, a preference a person decides, or a question whose deciding evidence is out of reach. Put these and the bound at the top of the prototype. Done when a reader can tell what would count as an answer.
2. Make the smallest thing that can show that observation, in the medium of the question, marked as a prototype where it lives. By kind:
   - Logic behavior: keep the rules in one small part that does no display, apart from the page or printout around it. Drive it through the cases that are hard to reason about on paper: the normal path, the awkward edge, and an action that should be refused. Show the full state after each step.
   - UI preference: make contrasting options when a comparison helps answer the question. Vary the relevant structure (layout, information order, or main action), using realistic content.
   - Other media, such as copy, a paper form, or a process: draft contrasting options in their own medium, and name the evidence that would decide between them.

   Add tests, saved data, or error handling only when the question is about them or needs them, such as checking a rule across every short sequence of actions. Otherwise keep state in memory and skip polish. Done when the thing runs or can be inspected, or the bound is reached.
3. Observe and label. Run the cases or view the options, recording what was run and what was seen. Label each result:
   - Measured fact: an observation the agent made, with its conditions. It holds only for the cases tried.
   - Preference: a person's choice. The agent may recommend with reasons and supply measurements, and never records its own preference as the decision.
   - Not clear yet: the bound was reached, the observations conflict, or the deciding evidence is out of reach.

   Done when every result has one label and its limit.
4. Return a verdict: `yes`, `no`, the chosen option, or `not clear yet` with the next thing worth trying and the evidence it needs. For a measured question, return the supported answer with its limits; a preference or required external judgment waits for the person. Anything later copied from the prototype keeps a pointer to this evidence and goes through the normal verification and review of the work that uses it. Done when the caller can record the verdict or resume with the next experiment.

## Return to the caller

Return a compact record containing:

- Question: the decision it informs, its kind, the bound, and who judges.
- Prototype: where it is, how to run or open it, and its revision or checksum line.
- Results: each labeled measured fact, preference, or not clear yet, with conditions and limits.
- Verdict: proposed or stated, by whom, and the next experiment when not clear yet.

The caller selects the durable home, keeps or discards the prototype, and owns task state and project delivery.

## Attribution

Adapted from Matt Pocock's [prototype](https://github.com/mattpocock/skills/blob/main/skills/engineering/prototype/SKILL.md) with its logic and UI references, inspected from the local reference labeled 1.2.3. It inspired one-question throwaway work, logic kept apart from its page, structurally different UI variants (three by default, at most five), visible state, saved data only when the question needs it, and rewriting prototype code before it reaches production. Atlas adds tests and error handling when needed, non-code media, and labeled results including `not clear yet`. The URL is a locator, not a pinned revision; the [task evidence](https://github.com/somethingdarkside1/atlas-skills/blob/72e890a/notes/2026-09-17-review-verification-and-prototype-methods.md) identifies the inspected files.

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
