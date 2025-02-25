
# k-robot-lan

客服机器人DSL解释器

## 项目简介

k-robot-lan 是一个用于客服机器人的领域特定语言（DSL）解释器。它能够解析和执行特定的DSL脚本，以实现客服机器人的各种功能。

## 目录结构

```
.
├── .gitignore
├── .vscode/
│   ├── launch.json
│   └── settings.json
├── docs/
│   ├── report.md
│   ├── report.pdf
├── examples/
│   ├── eq.krl
│   ├── err.krl
│   ├── fibonacci.krl
│   └── frontend/
├── README.md
├── requirements.txt
├── src/
├── tests/
└── tmp/
```

## 安装

请确保您已安装 Python 3.7 或更高版本。

1. 克隆仓库：
    ```sh
    git clone https://github.com/yourusername/k-robot-lan.git
    cd k-robot-lan
    ```

2. 安装依赖：
    ```sh
    pip install -r requirements.txt
    ```

## 使用方法

您可以通过以下命令运行解释器：

```sh
python src/main.py examples/fibonacci.krl
```

## 贡献

欢迎贡献代码！请提交 Pull Request 或报告问题。

## 许可证

本项目采用 MIT 许可证。详情请参阅 LICENSE 文件。
