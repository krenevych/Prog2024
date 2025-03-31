class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"

    def __add__(self, other):
        # other - обʼєкт, що буде стояти правіше від операції +
        if isinstance(other, Vector2D):
            return Vector2D(    # я тут припустив, що other обʼєкт типу Vector2D
                self.x + other.x,
                self.y + other.y
            )
        elif isinstance(other, (int, float)):
            return Vector2D(
                self.x + other,
                self.y + other
            )
        elif isinstance(other, (list, tuple)):
            if len(other) == 2:
                return Vector2D(
                    self.x + other[0],
                    self.y + other[1]
                )

        raise ValueError("Не підтримуваний тип даних справа у операції +")

if __name__ == '__main__':
    v1 = Vector2D(2, 3)
    v2 = Vector2D(1, 4)

    print(v1)
    print(v2)

    # v = v1.__add__(v2)
    v = v1 + v2  # Vector2D(3, 7)
    print(v)

    v3 = v + 4
    print(v3)
    v4 = v + (5, 6)
    print(v4)

    v5 = v + "шопопало"



