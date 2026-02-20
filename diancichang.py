import numpy as np

# --- 1. 秘方准备 (Setup) ---
size = 100
x = np.linspace(-2, 2, size)
y = np.linspace(-2, 2, size)
X, Y = np.meshgrid(x, y)

# 计算网格间距 (Grid spacing) —— 积分需要用到 "dx" 和 "dy"
dx = x[1] - x[0]
dy = y[1] - y[0]

# --- 2. 场计算 (Field Calculation) ---
r1 = np.sqrt((X + 0.5)**2 + Y**2) + 0.1
r2 = np.sqrt((X - 0.5)**2 + Y**2) + 0.1
Phi = (1.0 / r1) - (1.0 / r2)

# 计算梯度 (Gradient) 得到电场强度 E
# np.gradient 返回两个矩阵：x方向和y方向的斜率
Ex, Ey = np.gradient(-Phi, dx, dy)

# --- 3. 向量化计算能量 (Vectorized Energy Calculation) ---
# 计算每个点的电场强度的平方: E_squared = Ex^2 + Ey^2
E_squared = Ex**2 + Ey**2

# 总能量 W = 0.5 * epsilon_0 * sum(E^2 * dx * dy)
# 咱们假设 epsilon_0 = 1 (简化计算)
# np.sum 是向量化的求和，瞬间加总 10,000 个格子的值
total_energy = 0.5 * np.sum(E_squared) * dx * dy

print(f"--- 电气工程计算报告 ---")
print(f"分析网格密度: {size} x {size}")
print(f"计算得到的静电场总能量 W = {total_energy:.4f} Joules")
print("love gemini")
print("START!NOW!go exploreqq")