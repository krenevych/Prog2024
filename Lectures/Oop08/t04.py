class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return f"Vector2D({self.x}, {self.y}), {super().__str__()}"

    def __add__(self, other): # операція +
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

    def __isub__(self, other): # операція -=
        if isinstance(other, Vector2D):
            self.x -= other.x
            self.y -= other.y
        elif isinstance(other, (int, float)):
            self.x -= other
            self.y -= other
        elif isinstance(other, (list, tuple)):
            if len(other) == 2:
                self.x -= other[0]
                self.y -= other[1]
            else:
                raise ValueError("Кількість елементів у кортежі/списку справа не дорівнює 2!!")
        else:
            raise ValueError("Справа не підтримуваний тип!!")

        return self

    def __eq__(self, other):
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        else:
            return False

if __name__ == '__main__':
    v1 = Vector2D(1, 1)
    v2 = Vector2D(1, 1)
    print(v1)
    print(v2)

    print(v1 == v2)
    print(v1 != (1, 1))

    print(Vector2D(2, 3) != Vector2D(2, 3))
    print(Vector2D(2, 3) != Vector2D(1, 1))




