from pathlib import Path

import numpy as np

from mmcs import regression_chart, save_figure

root = Path(__file__).parent

np.random.seed(12)
x = np.random.uniform(3, 10, size=50)
y = x + np.random.uniform(-2, 4, size=50)

result = regression_chart(
    x=x,
    y=y,
    xlabel="X Value",
    ylabel="Y Value",
    title="Linear Regression",
)

save_figure(result.fig, root / "img", "regression_graphpad")
