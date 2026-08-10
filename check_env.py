import subprocess
import sys
from importlib import metadata, util

for cmd in (['nvcc', '--version'], ['nvidia-smi']):
    try:
        subprocess.run(cmd)
    except FileNotFoundError:
        print(f'{cmd[0]} not found')

print(f'sys version: {sys.version}')

try:
    import torch
    cuda_is_available: bool = torch.cuda.is_available()
    print(f'torch.cuda.is_available(): {cuda_is_available}')
    print(f'torch.cuda.get_device_capability(): {torch.cuda.get_device_capability() if cuda_is_available else "N/A"}')
except Exception:
    print("torch not found")

packages = [
    'torch', 'torchcodec', 'torchvision', 'torchaudio', 'transformers',
    'flash_attn', 'vllm', 'tensorrt', 'tensorrt_llm', 'triton',
    'triton_python_backend_utils',
]
dist_names = metadata.packages_distributions()
for name in packages:
    if util.find_spec(name) is None:
        print(f'{name} not found')
        continue
    try:
        dist = dist_names.get(name, [name])[0]
        print(f'{dist}=={metadata.version(dist)}')
    except metadata.PackageNotFoundError:
        print(f'{name} version: unknown')

print()
for dist in sorted(metadata.distributions(), key=lambda d: d.metadata['Name'].lower()):
    print(f"{dist.metadata['Name']}=={dist.version}")
