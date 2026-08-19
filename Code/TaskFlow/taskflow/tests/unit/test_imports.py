"""Unit test harness proving module imports and quality check scripts."""

import subprocess
import sys


def test_package_imports():
    """Ensure core domain models, enums, errors, and ports import without issue."""
    import taskflow.domain.enums as enums
    import taskflow.domain.errors as errors
    import taskflow.domain.models as models
    import taskflow.ports.repositories as repos

    assert enums.Channel.EMAIL == "email"
    assert models.utcnow() is not None
    assert repos is not None
    assert errors is not None


def test_no_hardcoded_models():
    """Run scripts/check_no_hardcoded_models.py to verify no hardcoded model strings exist in src/."""
    result = subprocess.run(
        [sys.executable, "scripts/check_no_hardcoded_models.py"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"check_no_hardcoded_models failed: {result.stderr}"
