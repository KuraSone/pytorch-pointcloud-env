import subprocess
import sys
from collections.abc import Mapping
from importlib import metadata, util
from typing import Any

for cmd in (["nvcc", "--version"], ["nvidia-smi"]):
    try:
        subprocess.run(cmd, check=False)
    except FileNotFoundError:
        print(f"{cmd[0]} not found")

print(f"sys version: {sys.version}")
print()

if util.find_spec("torch") is not None:
    import torch

    cuda_is_available: bool = torch.cuda.is_available()
    print(f"torch.cuda.is_available(): {cuda_is_available}")
    print(
        f"torch.cuda.get_device_capability(): {torch.cuda.get_device_capability() if cuda_is_available else 'N/A'}"
    )
else:
    print("torch not found")
print()

packages: list[str] = [
    "flash_attn",
    "kaolin",
    "pyg_lib",
    "pytorch3d",
    "tensorrt",
    "tensorrt_llm",
    "torch",
    "torch_geometric",
    "torchaudio",
    "torchcodec",
    "torchvision",
    "triton",
    "triton_python_backend_utils",
    "transformers",
    "vllm",
]
if hasattr(metadata, "packages_distributions"):
    dist_names: Mapping[str, list[str]] = metadata.packages_distributions()
else:
    dist_names = {}
    for _raw_dist in metadata.distributions():
        _dist: Any = _raw_dist
        _metadata: Any = _dist.metadata
        for _mod in (_dist.read_text("top_level.txt") or "").split():
            dist_names.setdefault(str(_mod), []).append(_metadata["Name"])
found: list[str] = []
missing: list[str] = []
for name in sorted(packages):
    if util.find_spec(name) is None:
        missing.append(f"{name} not found")
        continue
    try:
        dist = dist_names.get(name, [name])[0]
        found.append(f"{dist}=={metadata.version(dist)}")
    except metadata.PackageNotFoundError:
        found.append(f"{name} version: unknown")
for line in found:
    print(line)
print()
for line in missing:
    print(line)
print()

_dists: list[Any] = list(metadata.distributions())
for dist in sorted(_dists, key=lambda d: str(d.metadata["Name"]).lower()):
    _dist_metadata: Any = dist.metadata
    print(f"{_dist_metadata['Name']}=={dist.version}")
