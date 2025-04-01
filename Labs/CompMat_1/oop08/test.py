class Rational:
    def __init__(self, n, d=1):
        # assert type(n) == int and type(d) == int and d > 0
        self.n = n
        # if d == 0:
        #     raise ValueError("знаменник не повинен бути нулем")
        self.d = d

    def __str__(self):
        return f"({self.n}/{self.d})"

    def __add__(self, other):
        d = self.d * other.d
        n = self.n * other.d + self.d * other.n
        return Rational(n, d)

    def __mul__(self, other):
        n = self.n * other.n
        d = self.d * other.d
        return Rational(n, d)


r = Rational(2, 3) + Rational(5) * Rational(5, 6)
print(r)  # (2/3)
