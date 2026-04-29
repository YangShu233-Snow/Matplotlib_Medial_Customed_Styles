# Introduction

非常感谢你愿意为本项目贡献代码与创意，MMCS 项目将因此受益良多。

本项目将 GraphPad Prism 简约风格在内的高质量学术图表样式封装为 Python 库 `mmcs`，
通过 Profile 预设 + Quick API + 底层渲染器 三层架构，实现了样式与图表类型的正交解耦。

无论是新增图表渲染器、调整 .mplstyle 样式参数、改进 Profile 预设，都欢迎你的补充与分享！

## 提交前准备

### 开发环境配置

在开始贡献之前，请确保你已经配置好了开发环境。

```bash
git clone https://github.com/YangShu233-Snow/Matplotlib_Medical_Customzied_Styles
cd Matplotlib_Medical_Customzied_Styles
pip install -e ".[dev]"
```

本项目使用 conda 环境进行开发：

```bash
conda create -n Matplotlib_Medial_Customized_Styles python=3.12
conda activate Matplotlib_Medial_Customized_Styles
pip install -e ".[dev]"
```

### 项目结构

```
mmcs/
  __init__.py           # 公开 API 入口
  _registry.py           # 样式注册表
  _context.py            # StyleContext — 动态样式注入
  _profile.py            # Profile 预设（12 个 preset）
  _quick_api/            # Quick API 编排层（11 个子模块）
    _bar.py, _box.py, _violin.py, ...
  charts/                # 底层渲染器（13 个模块）
    _bar.py, _boxplot.py, _violin.py, ...
  _utils/                # 工具函数
    _stats.py, _annotation.py, _export.py
  styles/                # .mplstyle 文件
    graphpad_prism/      # 3 个风格家族
    ggplot/
    deeptools/
examples/                # 示例脚本
docs/                    # 文档站（MkDocs Material）
tests/                   # 自动化测试
scripts/                 # 辅助脚本
```

### 运行自动化测试

在提交任何 Pull Request 之前，请务必在本地完整运行一遍检查：

```bash
./scripts/check.sh
```

该脚本会依次执行：

1. **ruff** — Python 代码风格检查（必需）
2. **pytest** — 自动化测试（必需，130+ 测试覆盖所有模块）

你也可以单独运行测试：

```bash
pytest -v                          # 全部测试
pytest tests/test_bar.py           # 指定测试文件
pytest test/test_examples.py -k bar  # 按关键字过滤
```

### Docstring 规范

所有公共 API 须遵循 Google-style docstring，与文档站自动生成保持一致。

```python
def render(ax, data, *, groups=None):
    """Short description.

    Args:
        ax: The matplotlib Axes to draw on.
        data: Bar heights, one value per bar.
        groups: X-axis tick labels for each bar.

    Returns:
        The matplotlib Axes with the chart drawn.
    """
```

### 提交类型

本项目欢迎的提交类型包括：

- **新增图表渲染器** — 在 `mmcs/charts/` 下新建渲染函数，在 `mmcs/_quick_api/` 下新增 Quick API wrapper
- **新增风格家族** — 通过 `./scripts/new_style.sh <style_name>` 创建，编写 `.mplstyle` 和 `metadata.json`
- **修改 .mplstyle 样式参数** — 优化颜色、线宽、字体等默认值
- **改进 Profile 预设** — 调整 `mmcs/_profile.py` 中的默认参数
- **Bug 修复** — 修正渲染 bug、测试 bug、文档笔误

可能会被拒绝的提交类型：

- 没有关联测试或文档的纯代码提交
- 违反架构设计原则的提交（如将样式逻辑硬编码到渲染器中）
- 提交信息模糊或缺失

### 提交规范

推荐使用 Conventional Commits 格式：

```
feat: add boxplot renderer with sample size annotation
fix: correct jitter placement for clustered columns
docs: update API reference for violin chart
refactor: consolidate KDE bandwidth logic into _stats.py
chore: bump version to 0.2.0
```

## 贡献流程

### 新增功能

1. Fork 本仓库
2. 新建功能分支（如 `feat-my-new-chart`）
3. 完成代码编写并确保 `./scripts/check.sh` 通过
4. 提交 Pull Request，等待审核

### Bug 修复

1. Fork 本仓库
2. 新建修复分支（如 `fix-boxplot-animation`）
3. 完成修复并确保 `./scripts/check.sh` 通过
4. 提交 Pull Request，等待审核

## 致谢

感谢每一位 MMCS 的贡献者，你的贡献与创意让更多人因此受益！

Heart~ <3 <3 <3
