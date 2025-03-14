import math

from Labs.CompMat_1.oop06.Figure import Figure
from turtle import * # Підключаємо модуль turtle

class Triangle(Figure):
    def __init__(self, x1, y1, x2, y2):
        super().__init__()

        self.__vertex1 = (x1, y1)  # позиція другої відносно першої вершини
        self.__vertex2 = (x2, y2)  # позиція третьої відносно першої вершини

    def draw(self):
        up() # перестраховка, якщо пензлик був опущений

        goto(self._calc_position(self.position))
        pencolor(self.color)

        down()

        # зміщені координати для vertex1
        # x, y = self.__position[0] + self.__vertex1[0], self.__position[1] + self.__vertex1[1]
        x, y = self._calc_position(self.__vertex1)
        setpos(x, y)

        # зміщені координати для vertex1
        # x, y = self.__position[0] + self.__vertex2[0], self.__position[1] + self.__vertex2[1]
        x, y = self._calc_position(self.__vertex2)
        setpos(x, y)

        setpos(self._calc_position(self.position))
        up()


if __name__ == '__main__':
    t = Triangle(100, 0, 100, 100)
    print(t)

    reset()  # Ініціалізуємо режим малювання
    speed(1)
    # тут малюємо
    t.draw()

    # t.position = (100, 150)
    # t.scale = (2, 2)
    t.rotation = math.radians(30)
    t.color = "blue"
    t.pivot = (50, 30)
    t.draw()

    # t.position = (100, 150)
    t.scale = (2, 2)
    t.rotation = math.radians(45)
    t.color = "red"
    t.pivot = (100, 100)
    t.draw()

    mainloop()       # Затримуємо вікно на екрані
