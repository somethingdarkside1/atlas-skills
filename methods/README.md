# Shared method sources

The canonical methods are [interviewing](interview.md), [diagnosis](diagnosis.md), [verification](verification.md), and [prototyping](prototype.md). Each states when to use it, what it needs, and what it returns. Its caller owns persistence, task state, and project delivery.

[consumers.json](consumers.json) is the authoritative source-to-consumer mapping, including the shared evidence helper. Run `python3 scripts/bundle-methods.py` to generate local copies inside consumer skills and `python3 scripts/bundle-methods.py --check` to detect stale or missing copies. Generated headers identify the source and SHA-256; edit the source, then regenerate. Each operation's pointer states when its method is needed. These are plain local references, with no sibling-skill invocation dependency.

The integrated candidate wires these sources into its operations. File-level packaging checks and scratch runs are recorded on work-skills/07; clean-profile host installation and public release remain separate acceptance work. No standalone method skill is advertised.
