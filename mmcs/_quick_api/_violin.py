from __future__ import annotations

from pathlib import Path
from typing import Any, Optional, Sequence, Union

import matplotlib.pyplot as plt
import numpy as np

from mmcs._context import StyleContext
from mmcs._quick_api import ChartResult, _handle_save, _label
from mmcs._registry import Style
from mmcs.charts import violin


def violin_chart(
    data: Any,
    groups: Optional[Sequence[str]] = None,
    *,
    style: Union[str, Style] = "graphpad_prism",
    save_as: Optional[Union[str, Path]] = None,
    figsize: Optional[tuple[float, float]] = None,
    dpi: int = 300,
    split: bool = False,
    split_labels: Optional[list[str]] = None,
    bandwidth: str = "scott",
    points: int = 60,
    widths: float = 0.7,
    cut: float = 1.5,
    show_n: bool = True,
    title: Optional[str] = None,
    ylabel: Optional[str] = None,
) -> ChartResult:
    """Create a violin plot.

    High-level API for KDE violin plots with optional split mode
    for paired comparisons.

    Args:
        data: One array per group. For split mode, a list of
            ``(low, high)`` tuples.
        groups: X-axis labels.
        style: Style family name.
        save_as: Path to save the figure.
        figsize: Figure dimensions.
        dpi: Output resolution.
        split: If True, draw split violins for paired comparisons.
        split_labels: Legend labels for the split halves.
        bandwidth: KDE bandwidth rule (``"scott"`` or ``"silverman"``).
        points: Number of KDE grid points.
        widths: Violin width fraction.
        cut: KDE grid extension factor.
        show_n: Annotate sample sizes.
        title: Chart title.
        ylabel: Y-axis label.

    Returns:
        A ``ChartResult`` with the rendered figure.
    """
    ctxt = StyleContext(style)
    ctxt.apply(plt.rcParams, "violin")
    if figsize is None:
        figsize = (5, 5)
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)

    if split:
        handles = violin.render_split(
            ax, data, points=points, widths=widths, cut=cut,
            bandwidth=bandwidth, labels=split_labels, show_n=show_n,
        )
        if split_labels:
            ax.legend(handles=handles, frameon=False, loc="upper right")
    else:
        violin.render(ax, data, points=points, widths=widths,
                      cut=cut, bandwidth=bandwidth, show_n=show_n)

    x_positions = np.arange(len(data))
    ax.set_xticks(x_positions)
    if groups is not None:
        ax.set_xticklabels(list(groups))

    _label(ax, ylabel=ylabel, title=title)
    _handle_save(fig, save_as)
    return ChartResult(fig, stats={"n_groups": len(data)})
