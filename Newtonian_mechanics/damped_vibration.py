# 減衰振動
# オイラー法

import numpy as np
import matplotlib.pyplot as plt


class DampedVibration():
    def __init__(self, b):
        self.mass = 1       # 質量
        self.x = 1          # 初期位置
        self.velo = 0       # 初期速度
        self.k = 1          # ばね定数
        self.b = b          # 空気抵抗係数
        self.x_list = []    # 各時刻の位置
        self.velo_list = [] # 各時刻の速度

    def eval_force(self, x, velo):
        force = -self.k * x -self.b * velo
        return force

    def euler_dynamics(self, dt):
        self.x_list.append(self.x)
        self.velo_list.append(self.velo)

        force = self.eval_force(self.x, self.velo)
        self.x += self.velo * dt
        self.velo += (force / self.mass) * dt


def plot_curvature(x_list, label):
    t_arr = np.arange(len(x_list))
    x_arr = np.array(x_list)
    plt.plot(t_arr, x_arr, label=label)


if __name__ == '__main__':
    num_time_steps = 1000
    dt = 0.05

    b_list = [0.2, 0.5, 1.0, 1.5, 2.0]
    x_list = []
    for b in b_list:
        system = DampedVibration(b=b)
        for i in range(num_time_steps):
            system.euler_dynamics(dt)
        x_list.append(system.x_list)

    for i, b in enumerate(b_list):
        plot_curvature(x_list[i], str(b))
    plt.legend()
    plt.show()