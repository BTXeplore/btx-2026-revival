import numpy as np
import matplotlib.pyplot as plt

# --- 1. 定义初始状态（向量部队） ---
# 定义一个向量 i=[1, 0]
v = np.array([1, 0])

# --- 2. 定义变换指令（矩阵） ---
# 我们先玩简单的：把空间顺时针旋转 90 度
# 矩阵的第一列是 i 变换后的位置，第二列是 j 变换后的位置
M = np.array([[0, 1],
              [-1, 0]])

# --- 3. 执行变换（矩阵相乘） ---
# 在 Python 里，@ 符号就是矩阵乘法的“开火”指令
v_transformed = M @ v

# --- 4. 可视化（把结果画出来） ---
plt.figure(figsize=(5, 5))
# 画出原始向量 (蓝色)
plt.quiver(0, 0, v[0], v[1], color='blue', angles='xy', scale_units='xy', scale=1, label='Original')
# 画出变换后的向量 (红色)
plt.quiver(0, 0, v_transformed[0], v_transformed[1], color='red', angles='xy', scale_units='xy', scale=1, label='Transformed')

# 设置网格，让你看清位置
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.grid(True)
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.legend()
plt.title("Matrix Transformation: Rotation")
plt.show()