#!/usr/bin/env bash
# PostToolUse(Edit|Write): format and autofix only the file that was just touched.
set -euo pipefail
FILE=$(jq -r '.tool_input.file_path // empty')
[[ "$FILE" == *.py ]] || exit 0
cd "$CLAUDE_PROJECT_DIR"
uv run ruff format "$FILE" >/dev/null 2>&1 || true
uv run ruff check --fix "$FILE" >/dev/null 2>&1 || true
