from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from mmcs import Style, save_figure
from mmcs.charts import clustered_columns

root = Path(__file__).parent
style = Style("graphpad_prism")

np.random.seed(12)

groups_data = [
    (
        "Group A", ["CON", "KO"],
        [np.random.normal(1200, 300, 15), np.random.normal(3500, 400, 15)],
    ),
    (
        "Group B", ["CON", "KO-1", "KO-2"],
        [np.random.normal(1500, 200, 20), np.random.normal(2200, 300, 20), np.random.normal(1000, 500, 20)],
    ),
    (
        "Group C", ["CON", "KO"],
        [np.random.normal(1100, 150, 15), np.random.normal(1050, 100, 15)],
    ),
]

style.apply(plt.rcParams, "bar_clustered_scatter")
fig, ax = plt.subplots(figsize=(8, 6))

clustered_columns.render(
    ax, groups_data,
    comparisons=[(0, 0, 1, 3), (1, 0, 1, 2), (1, 0, 2, 3)],
)

ax.set_ylabel("Value")
ax.set_title("Clustered Columns Scatter")

save_figure(fig, root / "img", "clustered_columns_graphpad")
