import numpy as np
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt

def my_func(x):
    return x ** 3 + 2 * x ** 2


if __name__ == "__main__":
    sp.init_printing()
    x_ = sp.Symbol("x")
    y = x_ ** 3 + 2 * x_ ** 2

    print(x_)
    print(y)
    print(sp.diff(y, x_))
    print(sp.diff(y, x_).subs({x_: 1}))

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


