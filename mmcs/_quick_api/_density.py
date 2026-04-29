from __future__ import annotations

from pathlib import Path
from typing import Any, Optional, Sequence, Union

import matplotlib.pyplot as plt

from mmcs._context import StyleContext
from mmcs._quick_api import ChartResult, _handle_save, _label
from mmcs._registry import Style
from mmcs.charts import density


def density_chart(
    data: Any,
    groups: Optional[Sequence[str]] = None,
    *,
    style: Union[str, Style] = "graphpad_prism",
    save_as: Optional[Union[str, Path]] = None,
    figsize: Optional[tuple[float, float]] = None,
    dpi: int = 300,
    bandwidth: str = "scott",
    fill: bool = True,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    title: Optional[str] = None,
) -> ChartResult:
    """Create a KDE density plot.

    Supports multiple groups with automatic color assignment.

    Args:
        data: One array per group.
        groups: Group labels for the legend.
        style: Style family name.
        save_as: Path to save the figure.
        figsize: Figure dimensions.
        dpi: Output resolution.
        bandwidth: KDE bandwidth rule.
        fill: Fill under the curves.
        xlabel: X-axis label.
        ylabel: Y-axis label.
        title: Chart title.

    Returns:
        A ``ChartResult`` with the rendered figure.
    """
    ctxt = StyleContext(style)
    ctxt.apply(plt.rcParams, "density")
    if figsize is None:
        figsize = (5, 5)
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)

    density.render(ax, data, labels=groups, bandwidth=bandwidth, fill=fill)

    _label(ax, xlabel=xlabel, ylabel=ylabel, title=title)
    _handle_save(fig, save_as)
    return ChartResult(fig, stats={"n_groups": len(data)})
