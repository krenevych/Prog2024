
def Sum(n=-1):
    S = 1
    k = 1
    yield S, k

    while k != n:
        k = k + 1
        S = S + k
        yield S, k


if __name__ == '__main__':
    for S, k in Sum(10):
        print(S, k)

    print("============================")
    for S, k in Sum(): # нескінченний генератор
        print(S, k)
        if k >= 20:
            break
