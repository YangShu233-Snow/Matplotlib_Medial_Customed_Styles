from __future__ import annotations

from typing import List, Optional

import numpy as np
from matplotlib.axes import Axes


def draw_sample_sizes(
    ax: Axes,
    data: List[np.ndarray],
    x_positions: np.ndarray,
    offset: Optional[float] = None,
    offset_factor: Optional[float] = None,
    fontsize: float = 10,
) -> None:
    for i, d in enumerate(data):
        n = len(d)
        top_val = np.max(d)

        if offset is not None:
            y_pos = top_val + offset
        elif offset_factor is not None:
            y_pos = top_val + float(np.std(d)) * offset_factor
        else:
            y_range = ax.get_ylim()[1] - ax.get_ylim()[0]
            y_pos = top_val + y_range * 0.02

        ax.text(
            x_positions[i],
            y_pos,
            f"n={n}",
            ha="center",
            va="bottom",
            fontsize=fontsize,
        )


def jitter(
    y: np.ndarray,
    r_x: float,
    r_y: float,
) -> np.ndarray:
    n = len(y)
    x = np.zeros(n)
    D_x = 2 * r_x
    D_y = 2 * r_y

    sorted_idx = np.argsort(y, kind="stable")
    placed: list[int] = []

    for idx in sorted_idx:
        y_i = float(y[idx])
        conflicts = []
        for p_idx in reversed(placed):
            if y_i - float(y[p_idx]) >= D_y:
                break
            conflicts.append(p_idx)

        if not conflicts:
            x[idx] = 0.0
            placed.append(idx)
            continue

        intervals = []
        for c_idx in conflicts:
            dy = y_i - float(y[c_idx])
            y_ratio_sq = (dy / D_y) ** 2
            if y_ratio_sq >= 1.0:
                continue
            dx = D_x * np.sqrt(1.0 - y_ratio_sq) + 1e-8
            x_c = float(x[c_idx])
            intervals.append((x_c - dx, x_c + dx))

        candidates = [0.0]
        for lo, hi in intervals:
            candidates.extend([lo, hi])
        candidates.sort(key=lambda v: (abs(v), v))

        chosen = 0.0
        for cand in candidates:
            if all(not (lo < cand < hi) for lo, hi in intervals):
                chosen = cand
                break

        x[idx] = chosen
        placed.append(idx)

    return np.asarray(x, dtype=float)
