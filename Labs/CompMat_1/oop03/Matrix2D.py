class Matrix2D:
    def __init__(self, *a):
        if len(a) == 1:  # один параметр, але може в ньому бути або масив або інша матриця
            pass
        elif len(a) == 4: # вхідний параметр - 4 числа, перші два - перший рядок, 3, 4 - другий рядок.
            pass
        elif len(a) == 0: # одинична матриця
            pass
        else:
            raise ValueError("По таких даних неможливо створити матрицю!")


if __name__ == '__main__':
    m = Matrix2D(1, 2, 3, 4)
    # m1 = Matrix2D(m)
    # m2 = Matrix2D(
    #     [
    #         [1, 2],
    #         [3, 4]
    #     ]
    # )
    # m3 = Matrix2D()
    m4 = Matrix2D(1, 2, 3)  #  має бути породжена помилка
    #
    # s1 = int("5")
    # s2 = int("5_hello")
