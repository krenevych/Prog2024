class Triangle:

    def check_triangle_existence(self, a, b, c):
        return a + b > c and a + c > b and b + c > a

    def __init__(self, a, b, c):

        assert self.check_triangle_existence(a, b, c), "Трикутник з такими сторонами не існує"


        # знак _ означає, що поле є прихованим
        self.__a = a  # атрибут чи поле - перша сторона трикутника
        self.__b = b  # атрибут чи поле - друга сторона трикутника
        self.__c = c  # атрибут чи поле - третя сторона трикутника

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def set_a(self, a):

        # Має бути перевірка, чи можемо ми створити трикутник
        # зі сторонами a, self._b, self._c
        assert self.check_triangle_existence(a, self.__b, self.__c), "Трикутник з такими сторонами не існує"

        self.__a = a

    def set_b(self, b):

        # Має бути перевірка, чи можемо ми створити трикутник
        # зі сторонами self._a, b, self._c
        assert self.check_triangle_existence(self.__a, b, self.__c), "Трикутник з такими сторонами не існує"

        self.__b = b

    def set_c(self, c):

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

    # print(t1.__a)

    t1.__a = 100500  # незаконно, бо поле __a є приватним, фактично створюється нове поле
    print(" t1.__a = ", t1.__a)
    print(" t1.__a (old) = ", t1._Triangle__a)  # доступ до зовсім прихованого поля __a
    t1.print()
