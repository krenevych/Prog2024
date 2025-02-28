from Labs.CompMat_1.oop03.Matrix2D import Matrix2D
from Labs.CompMat_1.oop03.Vector2D import Vector2D


class Solver:
    def __init__(self, a: Matrix2D, b: Vector2D):
        self.a = a
        self.b = b

    def __str__(self):
        return f"A:\n{self.a}\nb:{self.b}"

    def solve(self):
        if self.a.is_degenerate():
            return None

        d = self.a.det()
        m1 = Matrix2D(self.b, self.a.col(2))
        # print("=== m1 ====")
        # print(m1)
        d1 = m1.det() # визначник матриці, у якій замість першого стовпчика, стоїть self.b

        m2 = Matrix2D(self.a.col(1), self.b)
        # print("=== m2 ====")
        # print(m2)
        d2 = m2.det() # визначник матриці, у якій замість другого стовпчика, стоїть self.b
        x1 = d1 / d
        x2 = d2 / d

        return Vector2D(x1, x2)

if __name__ == '__main__':
    A = Matrix2D(1, 2, 2, 1)
    b = Vector2D(4, 5)
    s = Solver(A, b)
    # print(s)
    print("=== A ====")
    print(A)
    print("=== b ====")
    print(b)
    x = s.solve()
    print(x)
