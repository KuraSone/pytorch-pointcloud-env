# pytorch-pointcloud-env

预配置好点云相关依赖（PyTorch、torch-geometric、pytorch3d、kaolin、flash-attn 等）的 Python 环境模板，使用 [uv](https://docs.astral.sh/uv/) 管理依赖，支持 Windows 和 Linux（x86_64）上的 CPU 与多种 CUDA 环境。

[English](README.en.md)

> 项目要求 Python `>=3.9, <3.15`；各环境依赖组会进一步约束对应的 Python 版本。

## 快速开始

### 1. 安装 uv

Windows (PowerShell)：

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Linux：

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

其他安装方式见 [uv 官方文档](https://docs.astral.sh/uv/getting-started/installation/)。

### 2. 安装依赖

```bash
uv sync --group cu128
```

> **提示**：`cu128` 只是其中一种依赖组。根据你的平台和 CUDA 版本，可以选择：

| 依赖组        | 说明                                          | Python 版本 |
| ------------- | --------------------------------------------- | ----------- |
| `cpu`         | CPU（torch 2.8.0）                            | 3.12        |
| `cpu-latest`  | 最新 CPU 环境（torch >=2.14.1）               | 3.14        |
| `cu102`       | CUDA 10.2（torch 1.10.2）                     | 3.9         |
| `cu102-linux` | CUDA 10.2（torch 1.12.1，仅 Linux）           | 3.10        |
| `cu118`       | CUDA 11.8（torch 2.7.1）                      | 3.12        |
| `cu126`       | CUDA 12.6（torch 2.8.0）                      | 3.12        |
| `cu128`       | CUDA 12.8（torch 2.8.0）                      | 3.12        |

> 以上 CPU/CUDA 环境组互斥，只能选择一个。`cpu-latest` 包含 PyTorch、torchvision、torch-geometric 和 pytorch3d，但不包含 kaolin、pyg-lib 等扩展包。

### 3. 开发工具（可选）

`dev` 是 uv 默认安装的依赖组，包含 mypy、ruff、ty 等开发工具。仅安装运行环境时可跳过：

```bash
uv sync --no-default-groups --group cu128
```

## 验证环境

```bash
uv run --no-sync python check_env.py
```
