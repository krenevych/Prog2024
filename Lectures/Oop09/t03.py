def fact(n):
    i = 0
    f = 1
    yield f
    while i < n:
        i += 1
        f *= i
        yield f
    # return f

if __name__ == '__main__':

    f = fact(10)
    print(f)

    f_1 = next(f)
    print(f_1)

    f_1 = next(f)
    print(f_1)

    f_1 = next(f)
    print(f_1)

    f_1 = next(f)
    print(f_1)