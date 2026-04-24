from typing import Dict, List

from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import numpy as np

from pathlib import Path

root_path = Path(__file__).parent
# 修改为要求的样式文件路径
style_file = root_path / './assets/single_volinplot_chart.mplstyle'
plt.style.use(style_file)

def scott_MISE(
        data: List[np.ndarray]
    )->float:
    n_avg = np.mean(data)
    return float(n_avg ** (-1/5))

def draw_violinplot(
        ax: Axes, 
        data: List[np.ndarray], 
        points: int, 
        widths: float
    ):

    x_pos = np.arange(len(data))
    bw_method = scott_MISE(data)

    parts = ax.violinplot(
        data,
        x_pos,
        points=points,
        widths=widths,
        bw_method=bw_method,
        showextrema=False
    )

    # 从 rcParams 中读取样式并应用
    for pc in parts['bodies']:
        pc.set_facecolor(plt.rcParams['patch.facecolor'])
        pc.set_edgecolor(plt.rcParams['patch.edgecolor'])
        pc.set_linewidth(plt.rcParams['patch.linewidth'])
        pc.set_alpha(1)  # 移除默认透明度以匹配 GraphPad 风格

def draw_sample_sizes(ax: Axes, data: List[np.ndarray], x_positions: np.ndarray):
    """在每个小提琴上方标注样本量 n=xxx"""
    y_range = ax.get_ylim()[1] - ax.get_ylim()[0]
    offset = y_range * 0.02
    
    for i, d in enumerate(data):
        n = len(d)
        top_val = np.max(d)
        ax.text(
            x_positions[i], 
            top_val + offset, 
            f'n={n}', 
            ha='center', 
            va='bottom',
            fontsize=10
        )

def main():
    # --- config ---
    title = 'Standard Violin Plot'
    ylabel = 'Value'
    img_name = 'example'

    points = 60
    widths = 0.7
    show_n = True  # 是否展示样本量

    np.random.seed(12)
    data = [
        np.random.normal(200, 80, 200),
        np.random.normal(800, 500, 200),
        np.random.normal(600, 100, 200)
    ]

    # --- figure ---
    fig, ax = plt.subplots(
        figsize=(5, 5)
    )

    draw_violinplot(
        ax, data, points, widths
    )

    # 应用配置中的标签和标题
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    x_positions = np.arange(len(data))
    ax.set_xticks(x_positions)
    ax.set_xticklabels([f'Sample {i+1}' for i in range(len(data))])

    if show_n:
        draw_sample_sizes(ax, data, x_positions)

    save_dir = root_path / Path('./img')
    save_dir.mkdir(parents=True, exist_ok=True)
    save_paths = [save_dir / f"{img_name}.png", save_dir / f"{img_name}.pdf"]

    plt.tight_layout()
    for save_path in save_paths:
        plt.savefig(save_path, bbox_inches='tight')

if __name__ == '__main__':
    main()
