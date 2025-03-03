class Triangle:

    def check_triangle_existence(self, a, b, c):
        return a + b > c and a + c > b and b + c > a

    def __init__(self, a, b, c):
        assert self.check_triangle_existence(a, b, c), "Трикутник з такими сторонами не існує"
        # знак __ означає, що поле є прихованим
        self.__a = a  # атрибут чи поле - перша сторона трикутника
        self.__b = b  # атрибут чи поле - друга сторона трикутника
        self.__c = c  # атрибут чи поле - третя сторона трикутника

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):

        # Має бути перевірка, чи можемо ми створити трикутник
        # зі сторонами a, self._b, self._c
        assert self.check_triangle_existence(a, self.__b, self.__c), "Трикутник з такими сторонами не існує"

        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):

        # Має бути перевірка, чи можемо ми створити трикутник
        # зі сторонами self._a, b, self._c
        assert self.check_triangle_existence(self.__a, b, self.__c), "Трикутник з такими сторонами не існує"

        self.__b = b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c):
        # Має бути перевірка, чи можемо ми створити трикутник
        # зі сторонами self._a, self._b, c
        assert self.check_triangle_existence(self.__a, self.__b, c), "Трикутник з такими сторонами не існує"

        self.__c = c

    def print(self):
        print(f"triangle {self.__a}, {self.__b}, {self.__c}")


if __name__ == '__main__':
    t1 = Triangle(3, 4, 5)
    print("==== triangle =====")
    t1.print()

    print(t1.a)  # викликається функція def a(self)
    print(t1.b)  # викликається функція def b(self)
    print(t1.c)  # викликається функція def c(self)

    t1.a = 5
    t1.b = 6
    t1.c = 7

    print("==== triangle after change =====")
    t1.print()



