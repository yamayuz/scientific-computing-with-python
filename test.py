import sympy
 
# 変数宣言（x,yが利用できるように）
x, y = sympy.symbols('x,y')
 
# 整式を設定（べき乗：**）
f = x ** 2 - y ** 2
 
# 整式fを因数分解
print(sympy.factor(f))