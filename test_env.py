import sys
import torch

# 1. 看当前用的是哪个 Python（应该带 .venv）
print("Python 解释器：", sys.executable)

# 2. 看 torch 版本
print("torch 版本：", torch.__version__)

# 3. 让 torch 真正算点东西，证明它能用
x = torch.tensor([1.0, 2.0, 3.0])
print("tensor 求和：", x.sum().item())
