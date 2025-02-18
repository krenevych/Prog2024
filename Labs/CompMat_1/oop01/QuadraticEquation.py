class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        # self.d = self.b ** 2 - 4 * self.a * self.c # дискримінант - не можна,
        # # бо може порушитися цілісність даних, отже робимо метод

    def __str__(self):
        return f"{self.a}x^2 + {self.b}x + {self.c} = 0"

    def discriminant(self):
        return self.b ** 2 - 4 * self.a * self.c

    def show(self):
        print(self)

    def solutions_number(self):
        # залежить від дискримінанту
        return 0

    def solve(self):
        # треба буде дискримінант - будемо використовувати self.d
        return ()  # список чи кортеж розвʼязків


if __name__ == '__main__':  # блок тестування класу
    eq = QuadraticEquation(30, -92, 26)
    # eq.show()
    print(eq)
    print(f"дискримінант рівняння {eq} буде {eq.discriminant()}")
    # eq.discriminant() = 100500
    eq.a = 100560
    print(f"дискримінант рівняння {eq} буде {eq.discriminant()}")
    # r = str(eq)
    # print(r)
