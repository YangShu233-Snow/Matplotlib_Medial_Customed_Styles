from __future__ import annotations

from pathlib import Path
from typing import Any, Optional, Union

import matplotlib.pyplot as plt
import numpy as np

from mmcs._context import StyleContext
from mmcs._quick_api import ChartResult, _handle_save, _label
from mmcs._registry import Style
from mmcs.charts import scatter, scatter_clustered


def scatter_chart(
    x: Any,
    y: Any,
    *,
    style: Union[str, Style] = "graphpad_prism",
    save_as: Optional[Union[str, Path]] = None,
    figsize: Optional[tuple[float, float]] = None,
    dpi: int = 300,
    c: Any = None,
    s: float = 20.0,
    cmap: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    title: Optional[str] = None,
    **kwargs: Any,
) -> ChartResult:
    """Create a simple scatter plot.

    Args:
        x: X-coordinates.
        y: Y-coordinates.
        style: Style family name.
        save_as: Path to save the figure.
        figsize: Figure dimensions.
        dpi: Output resolution.
        c: Marker color(s).
        s: Marker area.
        cmap: Colormap for color-mapped plots.
        xlabel: X-axis label.
        ylabel: Y-axis label.
        title: Chart title.
        **kwargs: Passed through to the renderer.

    Returns:
        A ``ChartResult`` with the rendered figure.
    """
    ctxt = StyleContext(style)
    ctxt.apply(plt.rcParams, "scatter")
    if figsize is None:
        figsize = (5, 5)
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    scatter.render(ax, x, y, c=c, s=s, cmap=cmap, **kwargs)
    _label(ax, xlabel=xlabel, ylabel=ylabel, title=title)
    _handle_save(fig, save_as)
    return ChartResult(fig, stats={"n_points": len(np.asarray(x))})


def scatter_clustered_chart(
    x: Any,
    y: Any,
    *,
    style: Union[str, Style] = "graphpad_prism",
    save_as: Optional[Union[str, Path]] = None,
    figsize: Optional[tuple[float, float]] = None,
    dpi: int = 300,
    color_by_cluster: bool = True,
    show_convex_hull: bool = True,
    show_confidence_ellipse: bool = True,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    title: Optional[str] = None,
) -> ChartResult:
    """Create a DBSCAN-clustered scatter plot.

    Automatically estimates clusters and optionally draws convex
    hulls and confidence ellipses.

    Args:
        x: X-coordinates.
        y: Y-coordinates.
        style: Style family name.
        save_as: Path to save the figure.
        figsize: Figure dimensions.
        dpi: Output resolution.
        color_by_cluster: Color points by cluster label.
        show_convex_hull: Draw convex hull boundaries.
        show_confidence_ellipse: Draw 2-sigma confidence ellipses.
        xlabel: X-axis label.
        ylabel: Y-axis label.
        title: Chart title.

    Returns:
        A ``ChartResult`` with the rendered figure.
    """
    ctxt = StyleContext(style)
    ctxt.apply(plt.rcParams, "scatter")
    if figsize is None:
        figsize = (5, 5)
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)

    scatter_clustered.render(
        ax, x, y,
        color_by_cluster=color_by_cluster,
        show_convex_hull=show_convex_hull,
        show_confidence_ellipse=show_confidence_ellipse,
        xlabel=xlabel, ylabel=ylabel,
    )

    if title:
        ax.set_title(title)

    _handle_save(fig, save_as)
    return ChartResult(fig, stats={"n_points": len(np.asarray(x))})
