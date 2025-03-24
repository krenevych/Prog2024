class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

if __name__ == '__main__':
    print(
        abs(-5.6)
    )

    v = Vector2D(3, 4)
    print(
        abs(v)  # v.__abs__()
    )