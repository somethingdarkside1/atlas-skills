---
part: map-skill
date: 2026-09-11
status: accepted
---

# Diagrams are Mermaid inside the Markdown

Every diagram lives in the file it describes, as a Mermaid block, so it renders on GitHub, in editors, and in agent apps without a build step. D3 needs HTML and JavaScript, Structurizr and PlantUML need a renderer, and Excalidraw stores JSON; none of them keep the method as plain `.md`. The layout rules (one diagram per zoom level, seven to nine nodes, ids equal to section slugs, status colours) do the work a fancier tool would.
