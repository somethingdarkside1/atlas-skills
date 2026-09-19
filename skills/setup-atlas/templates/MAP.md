<!--
FORMAT. Atlas map format 3.
The map owns project responsibilities and their decision prerequisites. Group work by independently understandable outcomes or capabilities, using the project's language. Lifecycle stages, tools, departments, and file types are not default categories; use them as parts only when they have an independent outcome.
Each full ## part section has Id, Status, purpose, Needs, Open questions, Decisions, and Plan. Id is stable and globally unique. Existing maps without Id use the old heading-derived id until setup records it explicitly. Headings can then change without renaming tasks.
Needs lists parts whose decisions this part consumes. Plan points to the one brief/task folder. Optional Remaining work points to a known missing output for planning; it is not an unresolved design question. Optional Acceptance points to review evidence for the combined Outcome.
Status: sketched means direction remains open; decided means scope is settled enough for the next work; building means work or accepted-scope gaps remain; done requires current combined Outcome acceptance under plan/README.md. Empty plans and child/task counts cannot establish done.
Open questions hold material decisions only, with a pointer when a task owns the question. Mark a question (prototype) when making something is needed, or (later: trigger) when current work does not depend on it. Resolved answers move to the brief or a decision, with experiment evidence linked there.
The Mermaid diagram is a derived view of section ids, labels, statuses, and Needs edges, pointing from prerequisite to dependent. Use a legible layout appropriate to the graph. Validate ids, links, missing targets and cycles before deriving it. An empty map needs no diagram. External edges in a detail view remain links to their authoritative section.
Split a view when it becomes hard to navigate, not at a fixed count. Move full sections to map/<group>.md and leave labeled pointers at the former location. Each part has exactly one full section. Moving sections preserves ids, task paths, decisions, and inbound links. Creating new responsibilities is a scope change and requires explicit ownership for existing work; it is not a redraw.
-->

# {Project name}

{Who this project serves and what it is intended to achieve.}
