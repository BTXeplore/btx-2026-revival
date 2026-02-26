import numpy as np
import matplotlib.pyplot as plt

# 1. 定义空间网格
x, y = np.meshgrid(np.linspace(-2, 2, 20), np.linspace(-2, 2, 20))

# 2. 定义一个具有恒定旋度的流场
# f = -y (高度越高，向左吹越猛)
# g = x  (越往右走，向上吹越猛)
f = -y
g = x

# 3. 计算理论旋度： dg/dx - df/dy = 1 - (-1) = 2
# 这是一个处处旋转的场！

# --- 绘图 (EE 视角) ---
plt.figure(figsize=(7,7))
plt.quiver(x, y, f, g, color='blue', alpha=0.8)
plt.title("Vector Field with Constant Curl (f=-y, g=x)")
plt.xlabel("x (g is vertical push)")
plt.ylabel("y (f is horizontl push)")
plt.grid(True)
plt.show()