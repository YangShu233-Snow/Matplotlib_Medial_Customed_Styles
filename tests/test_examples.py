import os
import runpy
from pathlib import Path

import matplotlib.pyplot as plt
import pytest

PROJECT_ROOT = Path(__file__).parent.parent
EXAMPLES_DIR = PROJECT_ROOT / "examples"

example_files = list(EXAMPLES_DIR.glob("*.py"))


@pytest.mark.parametrize("example_path", example_files, ids=lambda x: x.stem)
def test_examples_run_without_errors(example_path, monkeypatch):
    """Test each example script runs without errors."""

    monkeypatch.setattr(plt, "show", lambda *args, **kwargs: None)

    original_cwd = os.getcwd()

    try:
        os.chdir(example_path.parent)
        runpy.run_path(example_path.name)
        plt.close("all")
    except Exception as e:
        pytest.fail(f"Failed to execute {example_path.name}: {e}")
    finally:
        os.chdir(original_cwd)
