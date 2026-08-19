#!/usr/bin/env python3
"""Script to verify that model names (claude, qwen, gpt, llama) are not hardcoded in src/."""

import re
import sys
from pathlib import Path

MODEL_PATTERNS = [
    re.compile(r"claude-", re.IGNORECASE),
    re.compile(r"qwen", re.IGNORECASE),
    re.compile(r"gpt-", re.IGNORECASE),
    re.compile(r"\bllama", re.IGNORECASE),
]

# Allow config files/modules if any exist inside src
ALLOWED_PATHS = [
    "src/taskflow/config/",
]


def check_file(path: Path) -> list[str]:
    path_str = str(path)
    if any(allowed in path_str for allowed in ALLOWED_PATHS):
        return []

    violations = []
    try:
        content = path.read_text(encoding="utf-8")
        for line_idx, line in enumerate(content.splitlines(), 1):
            for pattern in MODEL_PATTERNS:
                if pattern.search(line):
                    violations.append(f"{path}:{line_idx}: {line.strip()}")
    except Exception as e:
        violations.append(f"Could not read {path}: {e}")

    return violations


def main() -> int:
    src_dir = Path("src")
    if not src_dir.exists():
        print("src/ directory not found", file=sys.stderr)
        return 1

    violations: list[str] = []
    for py_file in src_dir.rglob("*.py"):
        violations.extend(check_file(py_file))

    if violations:
        print("ERROR: Found hardcoded model strings in src/:", file=sys.stderr)
        for v in violations:
            print(f"  {v}", file=sys.stderr)
        return 1

    print("SUCCESS: No hardcoded model names found in src/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
