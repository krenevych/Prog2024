


class Triangle:

    # статична змінна-поле, що існує з класом, а не з обʼєктом
    triangles_counter = 0

    def __init__(self, a, b=0.0, c=0.0):
        self.id = Triangle.triangles_counter
        Triangle.triangles_counter += 1
        if isinstance(a, Triangle):
            self.a = a.a
            self.b = a.b
            self.c = a.c
        else:
            assert isinstance(a, (float, int)) and isinstance(b, (float, int))  and isinstance(c, (float, int))
            self.a = a  # атрибут чи поле - перша сторона трикутника
            self.b = b  # атрибут чи поле - друга сторона трикутника
            self.c = c  # атрибут чи поле - третя сторона трикутника


    def print(self):
        print(f"triangle {self} {self.id=}: {self.a}, {self.b}, {self.c}")


if __name__ == '__main__':

    print(Triangle.triangles_counter)

    t1 = Triangle(3, 4, 5)
    print("==== t1 =====")
    t1.print()


    t2 = Triangle(t1)  # створення нового трикутника t2, на базі попереднього t1
    print("==== t2 =====")
    t2.print()







