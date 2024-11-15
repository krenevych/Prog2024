def readMatrix(n): # n - кількість рядків матриці
    M = [] # матриця - списко списків, список рядків матриці
    for i in range(n):
        v = [float(el) for el in input().split()]
        M.append(v)

    return M

def writeMatrix(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j], end=" ")
        print()

def multiply(a, b):
    if len(a[0]) != len(b):
        return None

    c = []
    for i in range(len(a)):
        row = [0] * len(b[0])
        c.append(row)
    # print(c)

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                c[i][j] += a[i][k] * b[k][j]

    return c


######## main ############
if __name__ == '__main__':
    n_a, m_a = [int(el) for el in input().split()]
    a = readMatrix(n_a)
    n_b, m_b = [int(el) for el in input().split()]
    b = readMatrix(n_b)

    c = multiply(a, b)
    if c is None:
        print(-1)
    else:
        print(len(c), len(c[0]))
        writeMatrix(c)
    #
    # print(n_a, m_a)
    # print(n_b, m_b)
    # writeMatrix(a)
    # writeMatrix(b)
