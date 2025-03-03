class Triangle:

    def check_triangle_existence(self, a, b, c):
        return a + b > c and a + c > b and b + c > a

    def __init__(self, a, b, c):

        assert self.check_triangle_existence(a, b, c), "Трикутник з такими сторонами не існує"


        # знак _ означає, що поле є прихованим
        self._a = a  # атрибут чи поле - перша сторона трикутника
        self._b = b  # атрибут чи поле - друга сторона трикутника
        self._c = c  # атрибут чи поле - третя сторона трикутника

    def get_a(self):
        return self._a

    def get_b(self):
        return self._b

    def get_c(self):
        return self._c

    def set_a(self, a):

        # Має бути перевірка, чи можемо ми створити трикутник
        # зі сторонами a, self._b, self._c
        assert self.check_triangle_existence(a, self._b, self._c), "Трикутник з такими сторонами не існує"

        self._a = a

    def set_b(self, b):

        # Має бути перевірка, чи можемо ми створити трикутник
        # зі сторонами self._a, b, self._c
        assert self.check_triangle_existence(self._a, b, self._c), "Трикутник з такими сторонами не існує"

        self._b = b

    def set_c(self, c):

        # Має бути перевірка, чи можемо ми створити трикутник
        # зі сторонами self._a, self._b, c
        assert self.check_triangle_existence(self._a, self._b, c), "Трикутник з такими сторонами не існує"

        self._c = c


    def print(self):
        print(f"triangle {self._a}, {self._b}, {self._c}")


if __name__ == '__main__':
    t1 = Triangle(3, 4, 5)
    print("==== triangle =====")
    t1.print()
    #
    # t1._a = 100500  # незаконно, бо поле _a є приватним
    # t1.print()
    #
    # print(t1._a) # незаконно, бо поле _a є приватним
    # print(t1.get_a()) # законно, бо метод get_a() є публічним, бо його назва не починається зі знаку _

    # t1.set_a(100500)
    # t1.set_b(100500)
    t1.set_c(100500)
    t1.print()