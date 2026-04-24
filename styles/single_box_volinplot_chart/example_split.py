import matplotlib.pyplot as plt
import numpy as np

from pathlib import Path
from typing import List
from matplotlib.axes import Axes

root_path = Path(__file__).parent
# 修改为要求的样式文件路径
style_file = root_path / './assets/single_box_volinplot_chart.mplstyle'
plt.style.use(style_file)

def scott_MISE(data: List[np.ndarray]) -> float:
    n_avg = np.mean([len(d) for d in data])
    return float(n_avg ** (-1/5))

def draw_split_box_violinplot(
        ax: Axes, 
        data: List[np.ndarray], 
        points: int, 
        v_widths: float, 
        b_widths: float, 
        labels: List[str]
    ):
    x_pos = np.arange(len(data))
    bw_method = scott_MISE([np.concatenate(d) for d in data])

    low_group = [sub_data[0] for sub_data in data]
    high_group = [sub_data[1] for sub_data in data]

    prop_cycle = plt.rcParams['axes.prop_cycle']
    colors = [c['color'] for c in prop_cycle]

    handles = []
    for i, (side, group) in enumerate(zip(('low', 'high'), (low_group, high_group))):
        color = colors[i % len(colors)]
        
        # 绘制背景的半边小提琴图
        parts = ax.violinplot(
            group, positions=x_pos, points=points, widths=v_widths, 
            bw_method=bw_method, side=side, showextrema=False
        )
        for pc in parts['bodies']:
            pc.set_facecolor(color)
            pc.set_edgecolor('black')
            pc.set_linewidth(1.5)
            pc.set_alpha(1)
        
        # 为了与半边小提琴对齐，对箱线图的中心位置进行轻微偏移
        shift = -v_widths/4 if side == 'low' else v_widths/4
        box_pos = x_pos + shift
        
        # 绘制叠加的窄箱体
        ax.boxplot(
            group, positions=box_pos, widths=b_widths, showfliers=False, 
            patch_artist=plt.rcParams['boxplot.patchartist'], 
            boxprops=dict(facecolor='black')
        )
        
        # 记录图例信息
        from matplotlib.patches import Patch
        handles.append(Patch(facecolor=color, edgecolor='black', label=labels[i]))
        
    return handles

def draw_sample_sizes(ax: Axes, data: List[List[np.ndarray]], x_positions: np.ndarray):
    """在每个分离叠加图上方标注样本量 n=x/y"""
    y_range = ax.get_ylim()[1] - ax.get_ylim()[0]
    offset = y_range * 0.02
    
    for i, sub_data in enumerate(data):
        n_low = len(sub_data[0])
        n_high = len(sub_data[1])
        top_val = max(np.max(sub_data[0]), np.max(sub_data[1]))
        ax.text(
            x_positions[i], 
            top_val + offset, 
            f'n={n_low}/{n_high}', 
            ha='center', 
            va='bottom',
            fontsize=10
        )

def main():
    # --- config ---
    title = 'Split Box-Violin Plot'
    ylabel = 'Relative Expression'
    img_name = 'example_split'

    points = 60
    v_widths = 0.7
    b_widths = 0.08
    labels = ['Control', 'Treatment']
    show_n = True  # 是否展示样本量

    np.random.seed(12)
    # split 模式数据格式: [ [group1, group2], [group1, group2], ... ]
    data = [
        [np.random.normal(200, 50, 100), np.random.normal(250, 60, 100)],
        [np.random.normal(800, 150, 100), np.random.normal(700, 180, 100)],
        [np.random.normal(400, 80, 100), np.random.normal(500, 90, 100)]
    ]

    fig, ax = plt.subplots(figsize=(6, 5))

    handles = draw_split_box_violinplot(
        ax, data, points, v_widths, b_widths, labels=labels
    )
    ax.legend(handles=handles, frameon=False, loc='upper right')

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
