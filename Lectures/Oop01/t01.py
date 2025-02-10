# створення Класу, тобто шаблону по якому будуть створюватися трикутники
class Triangle:
    def __init__(self, a, b, c):
        self.a = a  # атрибут чи поле - перша сторона трикутника
        self.b = b  # атрибут чи поле - друга сторона трикутника
        self.c = c  # атрибут чи поле - третя сторона трикутника

    def print(self):
        print(f"triangle {self}: {self.a}, {self.b}, {self.c}")

t1 = Triangle(3, 4, 5)
t2 = Triangle(33, 44, 55)


# print(t1.a, t1.b, t1.c)
t1.print()
# print(t2.a, t2.b, t2.c)
t2.print()

t2.c = 66
# print(t2.a, t2.b, t2.c)
t2.print()
