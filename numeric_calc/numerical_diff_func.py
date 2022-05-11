# 微分係数算出（中心差分）
def calc_diff_c(func, x=1.0, dx=1e-4):
    return (func(x + dx) - func(x - dx)) / (2 * dx)


def my_func(x):
    return x ** 3 + 2 * x ** 2


if __name__ == "__main__":
    print(calc_diff_c(my_func))