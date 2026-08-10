# pytorch-pointcloud-env

A Python environment template with pre-configured point cloud dependencies (PyTorch, torch-geometric, pytorch3d, kaolin, flash-attn, etc.), managed with [uv](https://docs.astral.sh/uv/). Supports multiple CUDA versions and CPU-only setups.

[中文](README.md)

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

> **Note**: `cu128` is just one of the available dependency groups. Depending on your CUDA version and platform, you can choose:

| Group | Description | Python |
| --- | --- | --- |
| `cpu` | CPU only (torch 2.8.0) | 3.12 |
| `cu102` | CUDA 10.2 (torch 1.10.2) | 3.9 |
| `cu102-linux` | CUDA 10.2 (torch 1.12.1, Linux only) | 3.10 |
| `cu118` | CUDA 11.8 (torch 2.7.1) | 3.12 |
| `cu126` | CUDA 12.6 (torch 2.8.0) | 3.12 |
| `cu128` | CUDA 12.8 (torch 2.8.0) | 3.12 |

> The groups are mutually exclusive — pick exactly one.

## Verify the environment

```bash
uv run --no-sync python check_env.py
```
