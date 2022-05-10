import numpy as np
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt

def my_func(x):
    return x ** 3 + 2 * x ** 2


def check_err():
    df = pd.DataFrame()
    dx_list = np.linspace(0.0001, 1.0, 10)
    for dx in dx_list:
        err_f = (my_func(1.0 + dx) - my_func(1.0)) / dx - 7.0
        err_b = (my_func(1.0) - my_func(1.0 - dx)) / dx - 7.0
        err_c = (my_func(1.0 + dx) - my_func(1.0 - dx)) / (2 * dx) - 7.0
        err_f2 = (-3 * my_func(1.0) + 4.0 * my_func(1.0 + dx) - my_func(1.0 + 2 * dx)) / (2 * dx) - 7.0
        err_b2 = (3 * my_func(1.0) - 4.0 * my_func(1.0 - dx) + my_func(1.0 - 2 * dx)) / (2 * dx) - 7.0
        df.loc[dx, "forward"] = err_f
        df.loc[dx, "backward"] = err_b
        df.loc[dx, "central"] = err_c
        df.loc[dx, "forward2"] = err_f2
        df.loc[dx, "backward2"] = err_b2
    return df


if __name__ == "__main__":
    dx = 0.01

    # 前進差分
    df_dx_f = (my_func(1.0 + dx) - my_func(1.0)) / dx
    print(f'df_dx_f : {df_dx_f}')

    # 後進差分
    df_dx_b = (my_func(1.0) - my_func(1.0 - dx)) / dx
    print(f'df_dx_b : {df_dx_b}')

    # 中心差分
    df_dx_c = (my_func(1.0 + dx) - my_func(1.0 - dx)) / (2 * dx)
    print(f'df_dx_c : {df_dx_c}')

    # 2次精度前進差分
    df_dx_f2 = (-3 * my_func(1.0) + 4.0 * my_func(1.0 + dx) - my_func(1.0 + 2 * dx)) / (2 * dx)
    print(f'df_dx_f2 : {df_dx_f2}')

    # 2次精度後進差分
    df_dx_b2 = (3 * my_func(1.0) - 4.0 * my_func(1.0 - dx) + my_func(1.0 - 2 * dx)) / (2 * dx)
    print(f'df_dx_b2 : {df_dx_b2}')

    # dxを変化させたときの誤差をグラフ化
    err_df = check_err()
    err_df.plot()
    plt.show()