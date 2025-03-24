class RectTriangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"RectTriangle: {self.a}, {self.b}"

    def __bool__(self):
        a = self.a < 0
        b = self.b < 0
        return not (a or b)

    def __call__(self):
        return self.a * self.b * 0.5


if __name__ == '__main__':
    rt = RectTriangle(3, 4)
    s = str(rt)
    print(s)

    if rt:
        print(rt())
    else:
        raise ValueError("Трикутник містить відʼємні строни")

