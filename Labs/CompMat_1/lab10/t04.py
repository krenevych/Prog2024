def readMatrix():
    M = []
    for i in range(2):
        row = [float(el) for el in input().split()]
        M.append(row)

    return M

def det(M, c1, c2):
    res = M[0][c1] * M[1][c2] - M[0][c2] * M[1][c1]
    return res



# [           0    1     2
    # 0     [5.0, 8.0, 11.0]
    # 1     [-3.0, 6.0, 15.0]
# ]

############# main #################
A = readMatrix()
# print(A)
# print(det(A, 0, 1))
# print(det(A, 2, 1))
# print(det(A, 0, 2))
d = det(A, 0, 1)
x = det(A, 2, 1) / d
y = det(A, 0, 2) / d
print(f"{x:.3f}")
print(f"{y:.3f}")