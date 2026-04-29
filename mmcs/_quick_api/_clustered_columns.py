from __future__ import annotations

from pathlib import Path
from typing import Optional, Sequence, Union

import matplotlib.pyplot as plt
import numpy as np

from mmcs._context import StyleContext
from mmcs._quick_api import ChartResult, _handle_save, _label
from mmcs._registry import Style
from mmcs.charts import clustered_columns


def clustered_columns_chart(
    groups_data: Sequence[tuple[str, Sequence[str], Sequence[np.ndarray]]],
    *,
    comparisons: Optional[Sequence[tuple[int, int, int, int]]] = None,
    style: Union[str, Style] = "graphpad_prism",
    save_as: Optional[Union[str, Path]] = None,
    figsize: tuple[float, float] = (8, 6),
    dpi: int = 300,
    bar_width: float = 0.3,
    scatter_r: float = 1.5,
    ylabel: Optional[str] = None,
    title: Optional[str] = None,
) -> ChartResult:
    """Create a clustered column chart with jittered scatter overlay.

    Each category can have multiple sub-groups. Optionally draws
    comparison lines with significance stars.

    Args:
        groups_data: List of ``(category_name, sub_group_names,
            raw_data_arrays)`` tuples.
        comparisons: List of ``(cat_idx, sub_a, sub_b, n_stars)``
            tuples.
        style: Style family name.
        save_as: Path to save the figure.
        figsize: Figure dimensions.
        dpi: Output resolution.
        bar_width: Width of each bar.
        scatter_r: Marker radius for jittered points.
        ylabel: Y-axis label.
        title: Chart title.

    Returns:
        A ``ChartResult`` with the rendered figure.
    """
    ctxt = StyleContext(style)
    ctxt.apply(plt.rcParams, "bar_clustered_scatter")
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)

    clustered_columns.render(
        ax, groups_data,
        bar_width=bar_width,
        scatter_r=scatter_r,
        comparisons=comparisons,
    )

    _label(ax, ylabel=ylabel, title=title)
    _handle_save(fig, save_as)
    n_total = sum(len(sub) for _, sub, _ in groups_data)
    return ChartResult(fig, stats={"n_categories": len(groups_data), "n_subgroups": n_total})
