# ニュートン法により、2の平方根を求める
x = 5.0

while True:
    x2 = x - (x**2 - 2) / (x * 2)

    if abs(x2 - x) < 0.0001:
        break

    x = x2

print(x)