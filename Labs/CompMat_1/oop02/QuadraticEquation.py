class QuadraticEquation:

    INF = "Infinite number of solutions"

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        # self.d = self.b ** 2 - 4 * self.a * self.c # дискримінант - не можна,
        # # бо може порушитися цілісність даних, отже робимо метод

    def __str__(self):
        return f"{super().__str__()}: {self.a}x^2 + {self.b}x + {self.c} = 0"

    @property
    def discriminant(self):
        return self.b ** 2 - 4 * self.a * self.c

    def show(self):
        print(self)

    def solutions_number(self):
        solutions = self.solve()
        if solutions == QuadraticEquation.INF:
            return QuadraticEquation.INF
        return len(solutions)

    def solve(self):
        if self.a == 0: # лінійним випадок - вироджене квадратне рівняння
            if self.b == 0: # рівняння виду 0 = -c
                if self.c == 0: # рівняння виду 0 = 0
                    return QuadraticEquation.INF
                else: # рівняння що немає розвʼязків, наприклад 0 = 4
                    return () # множина розвʼязків порожня, отже повертаємо порожній кортеж
            else: # рівняння виду bx = -c, наприклад 4x = -9
                x1 = -self.c / self.b
                return (x1,)
        else:  # a != 0, повноцінне квадратне рівняння
            d = self.discriminant # маленька оптимізація, щоб не рахувати дискримінант багато разів.
            if d < 0: # розвʼязків немає
                return () # множина розвʼязків порожня, отже повертаємо порожній кортеж
            elif d == 0: # один розвʼязок
                x1 = -self.b / (2.0 * self.a)
                return (x1,)
            else: # d > 0, два розвʼязки
                d = d ** 0.5  # рахуємо корінь з дискримінанта, щоб потім в явному вигляді відшукання розвʼязків не робити цього.
                x1 = (-self.b + d) / (2.0 * self.a)
                x2 = (-self.b - d) / (2.0 * self.a)
                solutions = [x1, x2]
                solutions.sort()
                # return x1, x2
                return tuple(solutions)


if __name__ == '__main__':  # блок тестування класу
    eq1 = QuadraticEquation(0, 0, 0)
    print(eq1)
    print(eq1.solve())

    eq2 = QuadraticEquation(0, 0, 100500)
    print(eq2)
    print(eq2.solve())

    eq3 = QuadraticEquation(0, 2, 7)
    print(eq3)
    print(eq3.solve())

    eq4 = QuadraticEquation(1, 1, 7)
    print(eq4)
    print(eq4.solve())

    eq5 = QuadraticEquation(1, 4, 4)
    print(eq5)
    print(eq5.solve())

    eq6 = QuadraticEquation(1, -5, 6)
    print(eq6)
    print(eq6.solve())

    eq7 = QuadraticEquation(0, 0, 0)
    eq8 = QuadraticEquation(0, 0, 0)
    print(eq7)
    print(eq8)

    eq7.a = 5
    print(eq7)
    print(eq8)
