from pathlib import Path

import matplotlib.pyplot as plt
import pytest

PROJECT_ROOT = Path(__file__).parent.parent
STYLE_DIR = PROJECT_ROOT / "mmcs" / "styles"

style_files = list(STYLE_DIR.glob("**/*.mplstyle"))


@pytest.mark.parametrize("style_path", style_files, ids=lambda x: x.parent.parent.name)
def test_style_loads(style_path):
    """Test all .mplstyle files can be parsed and loaded correctly."""
    try:
        with plt.style.context(style_path):
            fig, ax = plt.subplots()
            ax.plot([1, 2, 3], [1, 4, 9])
            plt.close(fig)
    except Exception as e:
        pytest.fail(f"Failed to load style file {style_path.name}: {e}")
