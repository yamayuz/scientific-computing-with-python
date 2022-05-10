# SymPyはPythonで代数計算を行うためのライブラリ
import sympy as sp


# 使用する変数を定義する
x = sp.Symbol("x")
y = sp.Symbol("y")

# 数式を定義
f = (x + y)**3
g = 3 * x**2

# 変数に値を代入して評価できる
f_1_1 = f.subs([(x, 1), (y, 1)])
g_7 = g.subs(x, 7)
print(f'f(1, 1) = {f_1_1}')
print(f'g(7) = {g_7}')

# 式の展開
print(f'{f} = {sp.expand(f)}')

# 微分
df_dx = sp.diff(f, x)
dg_dx = sp.diff(g, x)
print(f'df_dx = {df_dx}')
print(f'dg_dx = {dg_dx}')