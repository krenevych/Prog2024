# Matrix input

def readMatrix(n): # n - кількість рядків матриці
    M = [] # матриця - списко списків, список рядків матриці
    for i in range(n):
        v = [float(el) for el in input().split()]
        M.append(v)

    return M

##### main ##########

A = readMatrix(3)
print(A)

# A =        0    1     2
    # [
# 0    #   [1.0, 3.0, 4.0],
# 1    #   [5.0, 6.0, 7.0],
# 2    #   [0.0, 9.0, 2.0]
    #   ]

print(A[1][2])