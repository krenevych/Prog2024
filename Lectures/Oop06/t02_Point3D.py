from Lectures.Oop06.t01_Point2D import Point2D


class Point3D(Point2D):

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self._z = z

    @property
    def z(self):
        return self._z

    def __str__(self):
        return f"Point3D: ({self.x}, {self.y}, {self.z})"

    def abs2(self):
        return super().abs2() + self.z ** 2


if __name__ == '__main__':
    z3 = Point3D(3, 4, 5)
    print(z3)
    # print(f"|z3|^2 =  {z3.abs2()}")
    print(f"|z3|   =  {z3.abs()}")
