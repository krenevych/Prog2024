# створення Класу, тобто шаблону по якому будуть створюватися трикутники
class Triangle:
    def __init__(self, a, b, c):
        assert a + b > c and b + c > a and a + c > b, "Такий трикутник створити не можливо"
        self.a = a  # атрибут чи поле - перша сторона трикутника
        self.b = b  # атрибут чи поле - друга сторона трикутника
        self.c = c  # атрибут чи поле - третя сторона трикутника

    def perimeter(self):
        return self.a + self.b + self.c

    def print(self):
        print(f"triangle {self}: {self.a}, {self.b}, {self.c}")

    def square(self):
        p = self.perimeter() / 2.0 # p - локальна змінна, що містить півпериметр
        s = p * (p - self.a) * (p - self.b) * (p - self.c)
        s = s ** 0.5
        return s

if __name__ == '__main__':
    t1 = Triangle(3, 4, 5)

    print(f"Периметр трикутника буде {t1.perimeter()}")
    print(f"Площа трикутника буде {t1.square()}")

    t2 = Triangle(5, 6, 7)
    t2.print()
    t2.a = 100500
    t2.print()
    print(f"Площа трикутника буде {t2.square()}")
    #
    # t3 = Triangle(5, 6, 56)
    # print(f"Площа трикутника буде {t3.square()}")




