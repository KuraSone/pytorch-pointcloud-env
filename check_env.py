import subprocess
import sys
from importlib import metadata, util

for cmd in (['nvcc', '--version'], ['nvidia-smi']):
    try:
        subprocess.run(cmd)
    except FileNotFoundError:
        print(f'{cmd[0]} not found')

print(f'sys version: {sys.version}')
print()

try:
    import torch
    cuda_is_available: bool = torch.cuda.is_available()
    print(f'torch.cuda.is_available(): {cuda_is_available}')
    print(f'torch.cuda.get_device_capability(): {torch.cuda.get_device_capability() if cuda_is_available else "N/A"}')
except Exception:
    print("torch not found")
print()

packages = [
    'torch', 'torchcodec', 'torchvision', 'torchaudio', 'transformers',
    'flash_attn', 'vllm', 'tensorrt', 'tensorrt_llm', 'triton',
    'triton_python_backend_utils',
]
dist_names = metadata.packages_distributions()
found, missing = [], []
for name in sorted(packages):
    if util.find_spec(name) is None:
        missing.append(f'{name} not found')
        continue
    try:
        dist = dist_names.get(name, [name])[0]
        found.append(f'{dist}=={metadata.version(dist)}')
    except metadata.PackageNotFoundError:
        found.append(f'{name} version: unknown')
for line in found:
    print(line)
print()
for line in missing:
    print(line)
print()

for dist in sorted(metadata.distributions(), key=lambda d: d.metadata['Name'].lower()):
    print(f"{dist.metadata['Name']}=={dist.version}")
