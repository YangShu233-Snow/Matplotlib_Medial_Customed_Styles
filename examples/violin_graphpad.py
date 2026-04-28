from pathlib import Path

import numpy as np

from mmcs import save_figure, violin_chart

root = Path(__file__).parent

np.random.seed(12)
data = [
    np.random.normal(200, 80, 200),
    np.random.normal(800, 500, 200),
    np.random.normal(600, 100, 200),
]

result = violin_chart(
    data=data,
    groups=[f"Sample {i+1}" for i in range(3)],
    ylabel="Value",
    title="Standard Violin Plot",
)

save_figure(result.fig, root / "img", "violin_graphpad")
