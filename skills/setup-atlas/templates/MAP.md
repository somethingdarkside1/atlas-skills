<!--
FORMAT. Agents: read this before editing. It is not rendered.
- Level 1: one paragraph on what this thing is and who or what it touches, then the diagram, then the parts. A map with no ## section yet is an empty map and carries no diagram.
- One ## section per part. The heading, lowercased with dashes, is the part id. Diagram node ids must match, and node labels are the headings.
- Each part carries, in this order: **Status:** sketched | decided | building | done. One purpose line. Needs: the ids of the parts that must be decided before this one, or none. Open questions. Decisions (links). Plan (link to plan/<part>/).
- An open question may start with a marker: (prototype) when only a made thing can answer it, (answered, see notes/<file>) once a prototype has, (later: <what will settle it>) when no work planned now depends on it.
- Part ids are unique across the whole map, including parts split into their own files. A split file starts with `part:` frontmatter and no status; the status line in this file is the truth, derived from the sub-parts: done when all are done, building when any is building, decided when all are at least decided, otherwise sketched.
- Seven to nine parts per diagram at most, flat, no subgraphs. When a part outgrows a screen, move its body to map/<part>.md (which gets its own diagram and sub-parts) and leave the status line and a link.
- The diagram is derived: a mermaid `flowchart LR` that opens with the four classDef lines below, then one node per section as `part-id["Heading"]:::status`, then one unlabelled edge per Needs entry pointing from the needed part to the part that needs it. Regenerate it from the sections, never the other way round.
    classDef sketched fill:#f4f4f4,stroke:#999,color:#333
    classDef decided fill:#dbeafe,stroke:#2563eb,color:#1e3a8a
    classDef building fill:#fef3c7,stroke:#d97706,color:#78350f
    classDef done fill:#dcfce7,stroke:#16a34a,color:#14532d
- A part section looks like this:
    ## Wordmark

    **Status:** sketched
    The studio name drawn as its own letterforms.
    Needs: none.
    Open questions: which surfaces matter most?
    Decisions: none yet.
    Plan: none yet.
-->

# {Project name}

{One paragraph: what this is, who and what it touches.}
