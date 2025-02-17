# створення Класу, тобто шаблону по якому будуть створюватися трикутники
class Triangle:
    def __init__(self, a, b, c):
        self.a = a  # атрибут чи поле - перша сторона трикутника
        new_a = a  # new_a це локальна змінна функції __init__
        self.b = b  # атрибут чи поле - друга сторона трикутника
        self.c = c  # атрибут чи поле - третя сторона трикутника

    def print(self):
        print(f"triangle {self}: {self.a}, {self.b}, {self.c}")

# a = 1
# def func():
#     global a
#     a = 23

if __name__ == '__main__':
    t1 = Triangle(3, 4, 5)
    # print(t1.c)
    t1.print()     # Triangle.print(t1)
    pass





