class Figure:
    def perimetr(self): pass
    def square(self): pass
    def volume(self) : pass
    def squareBase(self) : pass


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def _perimetr(self):
        return self.a + self.b + self.c

    def perimetr(self):
        return self._perimetr()

    def square(self):
        p = self._perimetr() / 2  # півпериметр
        a, b, c = self.a, self.b, self.c
        s = p * (p - a) * (p - b) * (p - c)
        return s ** 0.5

    def volume(self) : return None

class TrianglePyramid(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c) # створюємо трикутник, що є основою піраміди
        self.h = h

    def perimetr(self):
        return None

    def square(self):
        return None

    def volume(self):
        return 1/3 * self.h * super().square()



if __name__ == '__main__':
    # t = Triangle(3, 4, 5)
    # print(t.perimetr())
    # print(t.square())

    tp = TrianglePyramid(3, 4, 5, 3)
    print(tp.volume())
    print(tp.perimetr())
