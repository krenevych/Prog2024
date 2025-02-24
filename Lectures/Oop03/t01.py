# створення Класу, тобто шаблону по якому будуть створюватися трикутники
class Triangle:
    def __init__(self, a, b, c):
        self.a = a  # атрибут чи поле - перша сторона трикутника
        self.b = b  # атрибут чи поле - друга сторона трикутника
        self.c = c  # атрибут чи поле - третя сторона трикутника

    def print(self):
        print(f"triangle {self}: {self.a}, {self.b}, {self.c}")


if __name__ == '__main__':
    t1 = Triangle(3, 4, 5)
    print("==== t1 =====")
    t1.print()


    t2 = t1  # t2 - це інше імʼя для того ж трикутника, що і t1
    print("==== t2 =====")
    t2.print()

    t2.c = 100500  # обʼєкти в Python є MUTABLE
    print("==== t1 після зміни с =====")
    t1.print()
    print("==== t2 після зміни с =====")
    t2.print()





