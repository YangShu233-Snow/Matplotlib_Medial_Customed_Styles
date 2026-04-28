from pathlib import Path

import numpy as np

from mmcs import bubble_chart, save_figure

root = Path(__file__).parent

np.random.seed(12)
categories = [f"Sample {chr(65 + i)}" for i in range(13)]
x_values = np.random.normal(20, 10, len(categories))
bubble_sizes = np.random.normal(50, 20, len(categories))
color_values = np.random.randint(5, 100, len(categories)) / 1000

result = bubble_chart(
    categories=categories,
    x_values=x_values,
    bubble_sizes=bubble_sizes,
    color_values=color_values,
    style="ggplot",
    xlabel="Value",
    title="Bubble Plot",
)

save_figure(result.fig, root / "img", "bubble_ggplot", tight_layout=False)
