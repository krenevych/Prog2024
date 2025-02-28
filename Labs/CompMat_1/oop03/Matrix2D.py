from Labs.CompMat_1.oop03.Vector2D import Vector2D


class Matrix2D:
    def __init__(self, *a):
        if len(a) == 1:  # один параметр, але може в ньому бути або масив або інша матриця
            pass
        elif len(a) == 4:  # вхідний параметр - 4 числа, перші два - перший рядок, 3, 4 - другий рядок.
            # self.a11 = a[0]
            # self.a12 = a[1]
            # self.a21 = a[2]
            # self.a22 = a[3]

            self.a11, self.a12, self.a21, self.a22 = a

        elif len(a) == 0:  # одинична матриця
            self.a11, self.a12, self.a21, self.a22 = (1, 0,
                                                      0, 1)
        elif len(a) == 2: # приходить два вектори Vector2D
            if isinstance(a[0], Vector2D) and isinstance(a[1], Vector2D):
                self.a11, self.a21 = a[0].v1, a[0].v2
                self.a12, self.a22 = a[1].v1, a[1].v2
        else:
            raise ValueError("По таких даних неможливо створити матрицю!")

    def __str__(self):
        return f"{self.a11:3.2f} {self.a12:3.2f}\n{self.a21:3.2f} {self.a22:3.2f}"

    def col(self, num):
        if num == 1:
            return Vector2D(self.a11, self.a21)
        elif num == 2:
            return Vector2D(self.a12, self.a22)
        else:
            raise IndexError("Неправильний номер стовпчика")

    def det(self):
        return self.a11 * self.a22 - self.a12 * self.a21

    def is_degenerate(self):
        # return abs(self.det()) < 0.000001
        return self.det() == 0


if __name__ == '__main__':
    v1 = Vector2D(1, 2)
    v2 = Vector2D(3, 4)
    m = Matrix2D(v1, v2)
    print(m)

    b1 = m.col(2)
    print(b1)


    # m = Matrix2D(1, 2, 3, 4)
    # print(m)
    #
    # m1 = Matrix2D()
    # print(m1)
    # print(m1.det())
    # print(m1.is_degenerate())

    # m1 = Matrix2D(m)
    # m2 = Matrix2D(
    #     [
    #         [1, 2],
    #         [3, 4]
    #     ]
    # )
    # m3 = Matrix2D()
    # m4 = Matrix2D(1, 2, 3)  #  має бути породжена помилка
    #
    # s1 = int("5")
    # s2 = int("5_hello")






















