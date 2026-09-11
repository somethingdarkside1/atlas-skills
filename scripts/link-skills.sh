#!/usr/bin/env bash
# Symlink every skill in this repo into the local skill directories, so a
# `git pull` keeps installed skills current. Re-run after adding or renaming a skill.
set -euo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
for DEST in "$HOME/.claude/skills" "$HOME/.agents/skills"; do
  mkdir -p "$DEST"
  for skill in "$REPO"/skills/*/SKILL.md; do
    dir="$(dirname "$skill")"; name="$(basename "$dir")"
    ln -sfn "$dir" "$DEST/$name"
    echo "linked $name -> $DEST"
  done
done
