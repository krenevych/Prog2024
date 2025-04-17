

def f(x, n):
    xk = 1
    yield xk
    for k in range(1, n + 1):
        xk *= - x ** 2 / ((2 * k - 1) * 2 * k)

        yield xk


if __name__ == '__main__':
    x = float(input("x= "))
    n = int(input("n= "))

    # print(f(x, n)) # n-й член послідовності 11.1 b
    for elem in f(x, n):
        print(elem)