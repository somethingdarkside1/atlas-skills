# Local files are the truth; GitHub is a mirror

**Part:** side-skills

Matt Pocock's set makes the issue tracker configurable, so every skill carries GitHub, GitLab, and local-file branches and a setup skill has to be run first. Atlas keeps the plan as plain files in `plan/` and lets one optional skill, `/publish`, mirror tasks to GitHub issues one way, writing the issue numbers back. Every other skill knows only files, and a brand project or a CRM rollout gets the same method as a codebase.

Considered: GitHub-only (excludes non-code projects and people without a repo), configurable tracker (the abstraction Atlas exists to remove).
