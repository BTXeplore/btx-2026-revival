import numpy as np
import matplotlib.pyplot as plt

plt.ion()  # 开启交互模式（这是魔法开启的钥匙！）
fig, ax = plt.subplots(figsize=(6, 6))

v = np.array([1, 0])

for deg in range(0, 720, 5):  # 让它转两圈
    rad = np.radians(deg)
    # 旋转矩阵逻辑
    mat = np.array(((np.cos(rad), -np.sin(rad)), (np.sin(rad), np.cos(rad))))
    v_new = mat @ v

    ax.clear()  # 擦除上一帧（像翻页动画一样）
    ax.quiver(0, 0, v_new[0], v_new[1], angles='xy', scale_units='xy', scale=1, color='red')
    ax.set_xlim(-1.5, 1.5);
    ax.set_ylim(-1.5, 1.5)
    ax.grid(True)
    ax.set_title(f"3b1b Style Animation: Angle {deg}°")

    plt.pause(0.01)  # 暂停一小会，给大脑反应的时间

plt.ioff()
plt.show()