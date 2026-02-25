import numpy as np
import time

# ==========================================
# ⚡️ 首席架构师的实验：矩阵的“算子融合” ⚡️
# ==========================================

# 1. 准备材料：定义一个包含 100 万个相量的超大数组 (你的 100 万个轻骑兵)
# 每个相量是一个 2D 向量 [x, y]
num_soldiers = 1_000_000
vectors = np.random.rand(2, num_soldiers) # 形状是 2 行 1000万列

# 2. 定义两个“算子”：我们要转 30 度，然后再转 60 度
theta1 = np.radians(30)
theta2 = np.radians(60)

# 算子A：30度旋转矩阵
M1 = np.array([[np.cos(theta1), -np.sin(theta1)],[np.sin(theta1),  np.cos(theta1)]])

# 算子B：60度旋转矩阵
M2 = np.array([[np.cos(theta2), -np.sin(theta2)],[np.sin(theta2),  np.cos(theta2)]])

# ------------------------------------------
# ❌ 小白逻辑（不融合）：兵分两步，访存灾难
# ------------------------------------------
start_time = time.time()

# 第一步：100万个兵先乘 M1 (内存读写一次)
step1_result = M1 @ vectors
# 第二步：刚才的结果再乘 M2 (内存读写第二次)
final_dumb_result = M2 @ step1_result

time_dumb = time.time() - start_time
print(f"❌ 分步计算耗时: {time_dumb:.5f} 秒 (这就像是把猪肉拿出来切片，再放回冰箱，再拿出来绞碎)")

# ------------------------------------------
# ✅ 架构师逻辑（算子融合）：先融合理论，再发兵！
# ------------------------------------------
start_time = time.time()

# ⚡️ 核心黑魔法：我们先把 M2 和 M1 乘起来！
# 就像你说的 e^(i30) * e^(i60) = e^(i90)
# 我们把两个矩阵“融合”成了一个超级算子 M_fused
M_fused = M2 @ M1

# 所有的兵，只用这一个超级算子计算一次！（内存只读写一次）
final_smart_result = M_fused @ vectors

time_smart = time.time() - start_time
print(f"✅ 算子融合耗时: {time_smart:.5f} 秒 (融合了公式，只进行一次操作!q)")
print(f"🚀 速度提升了: {time_dumb / time_smart:.2f} 倍")