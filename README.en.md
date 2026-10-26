# pytorch-pointcloud-env

A Python environment template with pre-configured point cloud dependencies (PyTorch, torch-geometric, pytorch3d, kaolin, flash-attn, etc.), managed with [uv](https://docs.astral.sh/uv/). Supports CPU and multiple CUDA setups on Windows and Linux (x86_64).

[中文](README.md)

> The project requires Python `>=3.9, <3.15`; each environment dependency group further constrains its compatible Python version.

## Quick Start

### 1. Install uv

Windows (PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

See the [official uv docs](https://docs.astral.sh/uv/getting-started/installation/) for other installation methods.

### 2. Install dependencies

```bash
uv sync --group cu128
```

> **Note**: `cu128` is just one of the available dependency groups. Depending on your platform and CUDA version, you can choose:

| Group         | Description                                | Python |
| ------------- | ------------------------------------------ | ------ |
| `cpu`         | CPU only (torch 2.8.0)                     | 3.12   |
| `cpu-latest`  | Latest CPU setup (torch >=2.14.1)          | 3.14   |
| `cu102`       | CUDA 10.2 (torch 1.10.2)                   | 3.9    |
| `cu102-linux` | CUDA 10.2 (torch 1.12.1, Linux only)       | 3.10   |
| `cu118`       | CUDA 11.8 (torch 2.7.1)                    | 3.12   |
| `cu126`       | CUDA 12.6 (torch 2.8.0)                    | 3.12   |
| `cu128`       | CUDA 12.8 (torch 2.8.0)                    | 3.12   |

> The CPU/CUDA environment groups are mutually exclusive — pick exactly one. `cpu-latest` includes PyTorch, torchvision, torch-geometric, and pytorch3d, but not extension packages such as kaolin or pyg-lib.

### 3. Development tools (optional)

`dev` is uv's default dependency group and includes mypy, ruff, ty, and other development tools. To install only the runtime environment, skip it with:

```bash
uv sync --no-default-groups --group cu128
```

## Verify the environment

```bash
uv run --no-sync python check_env.py
```
