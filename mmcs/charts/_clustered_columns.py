from __future__ import annotations

from typing import Sequence

import numpy as np
from matplotlib.axes import Axes

from mmcs._utils._annotation import jitter


def render(
    ax: Axes,
    groups: Sequence[tuple[str, Sequence[str], Sequence[np.ndarray]]],
    *,
    bar_width: float = 0.3,
    scatter_r: float = 1.5,
    comparisons: Sequence[tuple[int, int, int, int]] | None = None,
) -> Axes:
    n_categories = len(groups)
    all_means: list[list[float]] = []
    all_errs: list[list[float]] = []
    all_raw: list[list[np.ndarray]] = []
    all_names: list[str] = []
    all_bar_pos: list[float] = []

    for cat_name, sub_names, raw_data_list in groups:
        means = [float(np.mean(d)) for d in raw_data_list]
        errs = [float(np.std(d, ddof=1) / np.sqrt(len(d))) for d in raw_data_list]
        all_means.append(means)
        all_errs.append(errs)
        all_raw.append([np.asarray(d).ravel() for d in raw_data_list])
        all_names.extend(sub_names)

    flat = [m for ms in all_means for m in ms]
    total = len(flat)

    x_base = np.linspace(0, (total + n_categories - 1) * bar_width * 2, total + n_categories)
    fig_w = ax.figure.get_figwidth() if hasattr(ax.figure, "get_figwidth") else 10
    fig_h = ax.figure.get_figheight() if hasattr(ax.figure, "get_figheight") else 6

    group_idx = 0
    for cat_idx in range(n_categories):
        means = all_means[cat_idx]
        errs = all_errs[cat_idx]
        raw = all_raw[cat_idx]
        n_sub = len(means)
        colors = [str(g) for g in np.linspace(0.1, 0.8, n_sub)]

        x_positions: list[float] = []
        for i in range(n_sub):
            x_pos = x_base[group_idx] + bar_width
            group_idx += 1
            x_positions.append(x_pos)
            all_bar_pos.append(x_pos)

            ax.bar(x_pos, means[i], yerr=[errs[i]], width=bar_width,
                   align="center", color=colors[i])

        for i, d in enumerate(raw):
            r_x = total / fig_w * scatter_r / 36
            r_y = max(flat) / fig_h * scatter_r / 36 if max(flat) != 0 else scatter_r / 36
            x_jit = jitter(d, r_x, r_y) + x_positions[i]
            ax.scatter(x_jit, d, color="white", edgecolor="black",
                       alpha=0.75, s=np.pi * scatter_r ** 2)

        group_idx += 1

    ax.set_xticks(x_base)
    ax.set_xticklabels([])
    ax.set_xlim(left=0)
    ax.set_ylim(bottom=0)
    ax.set_xticks(all_bar_pos, minor=True)
    ax.set_xticklabels(all_names, minor=True, rotation=45)

    if comparisons:
        cat_ranges: list[tuple[int, int]] = []
        start = 0
        for ms in all_means:
            cat_ranges.append((start, start + len(ms) - 1))
            start += len(ms)
        _draw_comparisons(ax, comparisons, all_bar_pos, all_raw, all_means, all_errs, cat_ranges)

    return ax


def _draw_comparisons(
    ax: Axes,
    comparisons: Sequence[tuple[int, int, int, int]],
    bar_pos: list[float],
    all_raw: list[list[np.ndarray]],
    all_means: list[list[float]],
    all_errs: list[list[float]],
    cat_ranges: list[tuple[int, int]],
) -> None:
    max_y_star = 0.0
    min_gap = 400

    for cat_idx, sub_a, sub_b, n_stars in comparisons:
        start, end = cat_ranges[cat_idx]
        x1, x2 = bar_pos[start + sub_a], bar_pos[start + sub_b]
        d_a = all_raw[cat_idx][sub_a]
        d_b = all_raw[cat_idx][sub_b]
        m_a, e_a = all_means[cat_idx][sub_a], all_errs[cat_idx][sub_a]
        m_b, e_b = all_means[cat_idx][sub_b], all_errs[cat_idx][sub_b]

        top = max(float(np.max(d_a)), m_a + e_a,
                  float(np.max(d_b)), m_b + e_b)

        line_y = top if top - max_y_star > min_gap else max_y_star + min_gap
        max_y_star = max(line_y, max_y_star)

        ax.plot([x1, x1, x2, x2],
                [line_y - 20, line_y, line_y, line_y - 20],
                c="black", linewidth=1.0)
        ax.text((x1 + x2) / 2, line_y, "*" * n_stars, ha="center", va="bottom")
