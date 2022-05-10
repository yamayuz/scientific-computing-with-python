# ニュートン法により、2の平方根を求める

def newton_method(x_ini, eps, max_iters=500):
    x, x_old = x_ini, x_ini
    iter_no, err = 0, 1
    while (err > eps):
        if x == 0:
            print("zero division err")
            break
        else:
            x = x - (x**2 - 2) / (2 * x)
        err = abs(x - x_old)
        print("iter: {:3d}, x: {:4f}, err: {:4f}".format(iter_no, x, err))
        x_old = x
        iter_no += 1
        if iter_no >= max_iters:
            break
    return x


if __name__ == "__main__":
    root2 = newton_method(5.0, 1e-4)
    print(root2)

    # x = 5.0
    # while True:
    #     x2 = x - (x**2 - 2) / (x * 2)

    #     if abs(x2 - x) < 0.0001:
    #         break

    #     x = x2
    # print(x)