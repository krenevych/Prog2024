from turtle import * # Підключаємо модуль turtle


class Triangle:

    def __init__(self, x1, y1, x2, y2):
        self.__position = (0, 0)   # абсолютна позиція першої вершини
        self.__vertex1 = (x1, y1)  # позиція другої відносно першої вершини
        self.__vertex2 = (x2, y2)  # позиція третьої відносно першої вершини

        self.color = "black"     # колір трикутника за промовчанням

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, pos):
        assert isinstance(pos, (tuple, list)) and len(pos) == 2
        self.__position = pos

    def __str__(self):
        return f"Triangle: {self.__position, self.__vertex1, self.__vertex2}"

    def draw(self):
        up() # перестраховка, якщо пензлик був опущений

        goto(self.__position)

        down()

        # зміщені координати для vertex1
        x, y = self.__position[0] + self.__vertex1[0], self.__position[1] + self.__vertex1[1]
        setpos(x, y)

        # зміщені координати для vertex1
        x, y = self.__position[0] + self.__vertex2[0], self.__position[1] + self.__vertex2[1]
        setpos(x, y)
        setpos(self.__position)
        up()


if __name__ == '__main__':
    t = Triangle(100, 0, 100, 100)
    print(t)

    reset()  # Ініціалізуємо режим малювання
    speed(1)
    # тут малюємо
    t.draw()


    # t.set_position(100, 100)
    # t.position = (100, 100, 100)
    # t.position = "green"
    t.position = (100, 150)
    t.draw()


    mainloop()       # Затримуємо вікно на екрані
