# Shared method sources

Canonical reasoning sources live here. Each source declares its trigger, inputs, process, and returned evidence. The caller owns persistence and state transitions. See [skill authoring](../skills/README.md) and the [shared methods brief](../plan/shared-methods/brief.md) for packaging ownership.

The table declares consumers for implemented sources. It is input to [task 05](../plan/shared-methods/05-bundle-method-references.md); generated references and installed operation wiring are pending that task and the work-skills migration. These source paths are repository authoring paths, not installed dependencies.

| Source | Consumer | Conditional load |
|---|---|---|
| [Diagnosis](diagnosis.md) | `build-it` | An observed failure needs explanation before choosing a correction. |
| [Diagnosis](diagnosis.md) | `review-it` | An unexplained regression prevents a justified finding or acceptance judgment. |
| [Diagnosis](diagnosis.md) | `interview-me` | A reported constraint may be an existing failure, and that distinction changes the scoped choice. |

No standalone method invocation is declared. The other method sources and their mappings remain with tasks 01, 03, and 04.
