import numpy as np
import matplotlib.pyplot as plt


class MyRand:
    def __init__(self, seed):
        self.A = 48271
        self.M = 2 ** 31 - 1
        self.seed = seed

    def rand(self, n):
        random_list = []
        for i in range(n):
            self.seed = (self.A * self.seed + 1) % self.M
            random_list.append(self.seed / self.M)
        return np.array(random_list)


if __name__ == "__main__":

    my_rand = MyRand(seed=123)
    x = my_rand.rand(n=100)
    y = my_rand.rand(n=100)

    plt.scatter(x, y)
    plt.show()