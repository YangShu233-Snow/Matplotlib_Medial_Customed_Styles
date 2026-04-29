from __future__ import annotations

from pathlib import Path
from typing import Any, Optional, Union

import matplotlib.pyplot as plt
import numpy as np

from mmcs._context import StyleContext
from mmcs._quick_api import ChartResult, _handle_save, _label
from mmcs._registry import Style
from mmcs.charts import histogram


def histogram_chart(
    data: Any,
    *,
    style: Union[str, Style] = "graphpad_prism",
    save_as: Optional[Union[str, Path]] = None,
    figsize: Optional[tuple[float, float]] = None,
    dpi: int = 300,
    bins: Optional[int] = None,
    bins_method: str = "freedman_diaconis",
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    title: Optional[str] = None,
) -> ChartResult:
    """Create a histogram.

    Uses the Freedman-Diaconis rule for automatic binning by default.

    Args:
        data: Input data values.
        style: Style family name.
        save_as: Path to save the figure.
        figsize: Figure dimensions.
        dpi: Output resolution.
        bins: Explicit number of bins. Auto-computed if ``None``.
        bins_method: Bin counting rule.
        xlabel: X-axis label.
        ylabel: Y-axis label.
        title: Chart title.

    Returns:
        A ``ChartResult`` with the rendered figure.
    """
    ctxt = StyleContext(style)
    ctxt.apply(plt.rcParams, "histogram")
    if figsize is None:
        figsize = (6, 4)
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)

    histogram.render(ax, data, bins=bins, bins_method=bins_method)

    _label(ax, xlabel=xlabel, ylabel=ylabel, title=title)
    _handle_save(fig, save_as)
    return ChartResult(fig, stats={"n_points": len(np.asarray(data).ravel())})
