def fact():
    # нескінченний генератор
    i = 0
    f = 1
    yield f
    while True:
        i += 1
        f *= i
        yield f


if __name__ == '__main__':
    for i in fact():
        if i > 10_000_000_000:
            break
        print(i)
