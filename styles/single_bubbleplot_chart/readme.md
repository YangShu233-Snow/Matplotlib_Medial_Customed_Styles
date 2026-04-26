# 气泡图 - R ggplot 风格 (Single Bubble Plot)

这是一个受 R `ggplot2` 启发的气泡图（Bubble Plot）样式，支持颜色映射与大小编码双变量展示，适用于富集分析（如 GO/KEGG）、基因表达等场景。

## 📊 效果预览

![Bubble Plot](./img/example.png)

## ✨ 核心特性

* **R ggplot 审美**：背景网格线、统一灰色图例散点，复刻 `ggplot2` 常见气泡图风格。
* **双变量编码**：气泡大小代表基因数量/表达值，颜色代表显著性（P 值）。
* **颜色高亮开关**：通过 `color_highlight` 控制是否启用彩色映射，关闭时使用统一灰色调。
* **P 值刻度支持**：内置标准 P 值阈值（0.001、0.005、0.01、0.05、0.1、0.5），通过 `p_value_ticks` 开关切换。
* **智能 X 轴范围**：内置 `calculate_x_lim` 自动计算对齐的 X 轴边界（10/100 取整）。
* **2×2 GridSpec 布局**：主图居左，图例与 Colorbar 分列右侧上下对齐。

## 🚀 快速运行

确保你已经激活了 Conda 环境。然后在当前目录下运行：

```bash
python example.py
```

运行后，图表将自动生成并保存在 `./img/` 中。

## 🛠️ 如何替换为你自己的数据？

打开 `example.py`，修改 `main` 函数中的配置和数据：

```python
# --- config ---
img_name = 'example'
title = 'Title'
legend_label = 'legend'
x_label  = 'Value'

color_highlight = True          # True: 彩色映射; False: 统一灰色
p_value_ticks = True            # True: colorbar 显示 P 值常用阈值 (0.001~0.5)
                                # False: colorbar 刻度在数据范围内均匀等分

# --- 气泡映射参数 ---
# bubble_size_data 中的数值越大 → 气泡越大; 数值越小 → 气泡越小
# 以下两个参数控制气泡在画布上实际占据的最小/最大面积 (point²)
min_bubble_size = 20
max_bubble_size = 100

# 图例展示哪几个分位数的气泡 (此处为最小值/中位数/最大值三档)
percentile = [0, 0.50, 1]

# --- 数据 (替换为你自己的数据即可) ---
categories = [str...]  # Y 轴标签

x_values = np.ndarray[...]   # 每个气泡的 X 坐标 (如富集分数)

# 决定气泡大小的变量
# 数值越大 → 气泡越
bubble_size_data = np.ndarray[...]

# 决定气泡颜色的变量
# 数值映射到红→紫色谱
# 图例显示对应 P_value
color_data = np.ndarray[...]
```
