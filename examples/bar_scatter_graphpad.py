from pathlib import Path

import numpy as np

from mmcs import bar_chart, save_figure

root = Path(__file__).parent

np.random.seed(12)
data_con = np.random.normal(1200, 300, 15)
data_ko = np.random.normal(3500, 400, 15)

means = [float(np.mean(d)) for d in [data_con, data_ko]]
errs = [float(np.std(d, ddof=1) / np.sqrt(len(d))) for d in [data_con, data_ko]]

result = bar_chart(
    data=means,
    groups=["Con", "KO"],
    errors=errs,
    stars=[0, 3],
    scatter_data=[data_con, data_ko],
    ylabel="Value",
    title="Bar Chart with Scatter",
)

save_figure(result.fig, root / "img", "bar_scatter_graphpad")
