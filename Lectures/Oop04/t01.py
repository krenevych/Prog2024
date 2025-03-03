class Triangle:

    def __init__(self, a, b, c):

        assert a + b > c and a + c > b and b + c > a, "Трикутник з такими сторонами не існує"

        self.a = a  # атрибут чи поле - перша сторона трикутника
        self.b = b  # атрибут чи поле - друга сторона трикутника
        self.c = c  # атрибут чи поле - третя сторона трикутника

    def print(self):
        print(f"triangle {self.a}, {self.b}, {self.c}")


if __name__ == '__main__':
    t1 = Triangle(3, 4, 5)
    print("==== triangle =====")
    t1.print()
