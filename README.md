<div align="center">
   
<img src='./assets/MMCS_LOGO.png' width=250>

# MMCS — Matplotlib Medical Customized Styles

🔬 **Reusable · Instant · Professional · Evolving** 🔬   
</div>

<div>
   <p align="center">
      <a href="https://github.com/YangShu233-Snow/Matplotlib_Medical_Customzied_Styles/actions/workflows/check.yaml">
         <img src="https://github.com/YangShu233-Snow/Matplotlib_Medical_Customzied_Styles/actions/workflows/check.yaml/badge.svg" alt="pytest">
      </a>
      <a href="https://matplotlib.org/">
         <img src="https://img.shields.io/badge/style-Matplotlib-blue?logo=python" alt="Matplotlib">
      </a>
      <a href="https://github.com/YangShu233-Snow/Matplotlib_Medical_Customzied_Styles/pulls">
         <img src="https://img.shields.io/badge/PRs-welcome-orange.svg" alt="pull requests">
      </a>
      <a href="./LICENSE">
         <img src="https://img.shields.io/github/license/YangShu233-Snow/Matplotlib_Medical_Customzied_Styles" alt="License">
      </a>
      <a href="https://github.com/YangShu233-Snow/Matplotlib_Medical_Customzied_Styles/commits/main">
         <img src="https://img.shields.io/github/last-commit/YangShu233-Snow/Matplotlib_Medical_Customzied_Styles" alt="Last Commit">
      </a>
      <a href="./llms.md">
         <img src="https://img.shields.io/badge/AI-Friendly-darkgreen" alt="AI Friendly">
      </a>
      <a href="https://pypi.org/project/mmcs/">
         <img src="https://img.shields.io/pypi/v/mmcs" alt="PyPI">
      </a>
   </p>
</div>

本项目将 **GraphPad Prism** 简约风格在内的高质量学术图表样式封装为 Python 库 `mmcs`。
无需手动调整繁琐的格式，只需一行代码即可生成符合高质量期刊出版要求的精美图表。

## 🎯 为什么要有这个仓库？

虽然 `matplotlib` 功能强大，但其默认样式不能满足大多数严肃科研工作场景的需求，而著名的样式库
[SciencePlots](https://github.com/garrettj403/SciencePlots) 所提供的样式拓展在生命科学与医学领域
有点水土不服。

本库旨在：

- 提供**可复用的出版级图表样式**（GraphPad Prism / ggplot2 / DeepTools）
- 通过 **Profile 预设**一键生成标准图表，零配置开箱即用
- 通过 **Quick API** 快速自定义，通过 **底层渲染器** 完全控制

期望本库能将你从繁杂的样式调整中解放，专注于数据本身。

## 🛠️ 快速上手

```bash
pip install mmcs
```

```python
import mmcs

# Profile 预设 — 零配置，一行出图
result = mmcs.profile.single_column(
    values=[1200, 3500],
    groups=["Control", "KO"],
    errors=[300, 400],
    save_as="output.png",
)
```

更多示例见 [文档站](docs/) 或 `examples/` 目录。

## 📁 包含的图表预设 (Profile Presets)

### GraphPad Prism 风格

| 预设 | 描述 | API |
| --- | --- | --- |
| 单列柱状图 | 经典的双组/多组比较柱状图，支持非对称误差线和显著性标注 | `mmcs.profile.single_column()` |
| 柱状散点图 | 柱状图叠加个体数据点 | `mmcs.profile.bar_scatter()` |
| 分簇柱状图 | 分组柱状图叠加抖动散点和组间比较线 | `mmcs.profile.grouped_columns()` |
| 箱线图 | 简约箱线图，自动标注样本量 | `mmcs.profile.boxplot()` |
| 小提琴图 | KDE 小提琴图，支持 Scott / Silverman 带宽优化 | `mmcs.profile.violin()` |
| 箱线+小提琴 | 箱线图与小提琴图叠加组合 | `mmcs.profile.box_violin()` |
| 散点与相关性 | DBSCAN 聚类散点图 / 线性回归散点图 | `mmcs.profile.scatter()` / `mmcs.profile.correlation()` |
| 直方图 | 直方图，内置 Freedman-Diaconis 准则自动分箱 | `mmcs.profile.histogram()` |
| 密度图 | KDE 密度分布图，平滑曲线与半透明填充 | `mmcs.profile.density()` |

### R ggplot 风格

| 预设 | 描述 | API |
| --- | --- | --- |
| 气泡图 | 多维度气泡图，支持大小和颜色双变量编码 | `mmcs.profile.bubble()` |

### DeepTools 风格

| 预设 | 描述 | API |
| --- | --- | --- |
| 热图 | 带聚类树的基因组学热图 | `mmcs.profile.heatmap()` |

## 🤖 AI friendly

本仓库对 AI 友好，如果你是 Agent 用户，或你的 AI 支持从链接读取本仓库内容，可以放心将仓库交给它解读。
作者已尽可能在 [llms.md](./llms.md) 中描述清楚本项目的结构。

## 🤝 贡献指南

欢迎提交 Issue 或 Pull Request 来添加新的学术图表风格！

如果你想为本项目提出 Pull Request，可以参照 [贡献指南](CONTRIBUTING.md)

## 🙇 致谢

非常感谢以下**项目/资料**，在开发 **MMCS** 时候，我从中得到了许多帮助：

- [From Data to Viz](https://www.data-to-viz.com/)
- [Matplotlib](https://matplotlib.org/)
- [GraphPad Prism](https://www.graphpad.com/)
- [DeepTools](https://github.com/deeptools/deepTools)

## 📄 License

MIT License
