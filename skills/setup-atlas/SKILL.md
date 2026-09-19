---
name: setup-atlas
description: Adopt Atlas in a new or existing project, preserving its work, formats, and delivery policy.
disable-model-invocation: true
---

# Set up Atlas

Create missing homes or explicitly upgrade an existing Atlas project. Use templates beside this file as starting formats, with the project's real content and conventions.

Read the project's purpose, existing homes and indices, applicable AGENTS.md/CLAUDE.md and their link relationship, and any existing task or delivery authority. Inspect existing changes before editing.

1. Establish the adoption scope from the request and existing authorization. Explain what is present and what needs creating or adapting. Resolve material conflicts, such as an existing hosted task authority or customized format with different semantics, before changing that authority; continue independent safe adoption where useful. Ordinary setup needs no Git account or tracker choice.
2. Create only missing homes. When a matching glossary, map, or work record already exists, adopt or link it under one authoritative location instead of copying live content into two homes. For a new project, start with its stated purpose; empty homes need no invented terms, parts, or tasks. Ask only for a missing purpose that cannot be inferred.
3. Upgrade owned format guidance from the templates while preserving project content, stable ids, historical evidence, and custom rules. Read [migration guidance](MIGRATION.md) for older formats or hosted tasks. Record old heading-derived part ids before renaming headings. A conflict leaves a precise pending action and the prior authority intact; a partial rerun resumes the recorded adoption.
4. Add or update the Atlas instruction section using templates/CLAUDE-block.md. Follow the actual project's instruction files: update a shared symlink target once; preserve distinct host-specific instructions and project additions. When neither file exists, create AGENTS.md as the common entry and link CLAUDE.md only when that host needs it. Keep delivery policy in its existing owner. The template supplies no automatic commit or publish rule.
5. Check the resulting links, unique owners, format compatibility, and instruction pointers. An unchanged rerun reports that setup is current. Save owned changes under project policy and report the actual diff or pending conflict. Finish with the next action for the requested work, or atlas for orientation.
