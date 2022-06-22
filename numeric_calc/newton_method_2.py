# ニュートン法により、3の平方根を求める

if __name__ == "__main__":
    x, x_old = 1.0, 1.0
    err = 1
    while (err > 1e-4):
        if x == 0:
            break
        else:
            x = x - (x**2 - 3) / (2 * x)
            err = abs(x - x_old)
            print(f'x: {x:4f}, err: {err:4f}')
            x_old = x

    print(f'x: {x}')