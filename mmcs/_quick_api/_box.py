from __future__ import annotations

from pathlib import Path
from typing import Any, Optional, Sequence, Union

import matplotlib.pyplot as plt

from mmcs._context import StyleContext
from mmcs._quick_api import ChartResult, _handle_save, _label, _resolve_frame
from mmcs._registry import Style
from mmcs.charts import boxplot


def box_chart(
    data: Any,
    *,
    x: Optional[str] = None,
    y: Optional[str] = None,
    groups: Optional[Sequence[str]] = None,
    style: Union[str, Style] = "graphpad_prism",
    save_as: Optional[Union[str, Path]] = None,
    figsize: Optional[tuple[float, float]] = None,
    dpi: int = 300,
    show_n: bool = True,
    patch_facecolor: str = "#CCCCCC",
    title: Optional[str] = None,
    ylabel: Optional[str] = None,
    **kwargs: Any,
) -> ChartResult:
    """Create a box plot.

    High-level API for box plots with optional sample size annotation.

    Args:
        data: One array per group, or a DataFrame.
        x: DataFrame column name for group labels.
        y: DataFrame column name for values.
        groups: X-axis labels for each box.
        style: Style family name.
        save_as: Path to save the figure.
        figsize: Figure dimensions.
        dpi: Output resolution.
        show_n: Annotate ``n=<count>`` above each box.
        patch_facecolor: Box fill color.
        title: Chart title.
        ylabel: Y-axis label.
        **kwargs: Passed through to the renderer.

    Returns:
        A ``ChartResult`` with the rendered figure.
    """
    arr, grp = _resolve_frame(data, x, y)
    ctxt = StyleContext(style)
    ctxt.apply(plt.rcParams, "boxplot")
    if figsize is None:
        figsize = (5, 5)
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    boxplot.render(ax, arr, labels=grp if grp is not None else groups,
                   show_n=show_n, patch_facecolor=patch_facecolor, **kwargs)
    _label(ax, ylabel=ylabel, title=title)
    _handle_save(fig, save_as)
    return ChartResult(fig, stats={"n_groups": len(arr)})
