class Point2D:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def abs2(self):
        return self.x ** 2 + self.y ** 2

    def abs(self):
        return self.abs2() ** 0.5

    def __str__(self):
        return f"Point2D: ({self.x}, {self.y})"


if __name__ == '__main__':
    z = Point2D(3, 4)
    print(z)
    print(f"|z|^2 =  {z.abs2()}")
    print(f"|z|   =  {z.abs()}")