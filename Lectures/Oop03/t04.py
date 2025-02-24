
# НЕ РОБОЧИЙ КОД - ДЛЯ РОЗУМІННЯ, ЩО ТАКЕ КОНСТРУКТОР КОПІЮВАННЯ
class Triangle:
    def __init__(self, a: число, b: число, c: число):
        self.a = a  # атрибут чи поле - перша сторона трикутника
        self.b = b  # атрибут чи поле - друга сторона трикутника
        self.c = c  # атрибут чи поле - третя сторона трикутника

    def __init__(self, t: Triangle):
        # створення трикутника н абазі t
        pass


    def print(self):
        print(f"triangle {self}: {self.a}, {self.b}, {self.c}")


if __name__ == '__main__':
    t1 = Triangle(3, 4, 5)
    print("==== t1 =====")
    t1.print()

    t2 = Triangle(t1)  # створення нового трикутника t2, на базі попереднього t1




