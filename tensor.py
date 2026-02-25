import numpy as np

# ==========================================
# ⚡️ 首席架构师：张量核心逻辑全解析 ⚡️
# ==========================================

# 1. 【创建】定义一个 Rank 3 张量 (信号立方体)
# 假设：3个频率波段(Channel), 每个波段 4个采样点(Time), 2个传感器(Sensor)
# 形状：(3, 4, 2)
signals = np.arange(24).reshape(3, 4, 2).astype(np.float32)

print(f"📡 原始信号立方体 (Shape: {signals.shape}):")
print(signals)

# 2. 【广播逻辑】给所有信号统一增加一个“环境噪声衰减”
# 虽然噪声只是一个数(标量)，但它会自动作用于所有 24 个点
noise_offset = 0.5
quiet_signals = signals - noise_offset

# 3. 【求和/缩并】计算每个频率波段的总能量
# axis=1 表示沿着“时间”维度进行塌缩
# 这在计算架构中叫 Reduction (规约运算)
energy_per_channel = np.sum(quiet_signals, axis=1)
print(f"\n📊 每个频段的能量分布 (Shape: {energy_per_channel.shape}):")
print(energy_per_channel)

# 4. 【张量点积】最硬核的优化：批量增益控制
# 假设我们要给 3 个频道分别乘以不同的增益系数 [1.0, 2.0, 0.5]
gains = np.array([1.0, 2.0, 0.5])

# 为了能和 (3, 4, 2) 的张量相乘，我们需要把 gains 的维度对齐
# (3,) -> (3, 1, 1) 这叫维度扩展 (NewAxis)
# 这样 gains 就会沿着时间轴和传感器轴自动“克隆”
gains_reshaped = gains[:, np.newaxis, np.newaxis]
final_output = quiet_signals * gains_reshaped

print(f"\n🚀 增益调整后的最终信号 (第一频段样例):")
print(final_output[0]) # 只打印第一个频道看看import numpy as np

# ==========================================
# ⚡️ 首席架构师：张量核心逻辑全解析 ⚡️
# ==========================================

# 1. 【创建】定义一个 Rank 3 张量 (信号立方体)
# 假设：3个频率波段(Channel), 每个波段 4个采样点(Time), 2个传感器(Sensor)
# 形状：(3, 4, 2)
signals = np.arange(24).reshape(3, 4, 2).astype(np.float32)

print(f"📡 原始信号立方体 (Shape: {signals.shape}):")
print(signals)

# 2. 【广播逻辑】给所有信号统一增加一个“环境噪声衰减”
# 虽然噪声只是一个数(标量)，但它会自动作用于所有 24 个点
noise_offset = 0.5
quiet_signals = signals - noise_offset

# 3. 【求和/缩并】计算每个频率波段的总能量
# axis=1 表示沿着“时间”维度进行塌缩
# 这在计算架构中叫 Reduction (规约运算)
energy_per_channel = np.sum(quiet_signals, axis=1)
print(f"\n📊 每个频段的能量分布 (Shape: {energy_per_channel.shape}):")
print(energy_per_channel)

# 4. 【张量点积】最硬核的优化：批量增益控制
# 假设我们要给 3 个频道分别乘以不同的增益系数 [1.0, 2.0, 0.5]
gains = np.array([1.0, 2.0, 0.5])

# 为了能和 (3, 4, 2) 的张量相乘，我们需要把 gains 的维度对齐
# (3,) -> (3, 1, 1) 这叫维度扩展 (NewAxis)
# 这样 gains 就会沿着时间轴和传感器轴自动“克隆”
gains_reshaped = gains[:, np.newaxis, np.newaxis]
final_output = quiet_signals * gains_reshaped

print(f"\n🚀 增益调整后的最终信号 (第一频段样):")
print(final_output[0]) # 只打印第一个频道看看