import math

from Labs.CompMat_1.oop06.Figure import Figure
from turtle import * # Підключаємо модуль turtle

class Triangle(Figure):
    def __init__(self, x0, y0, x1, y1, x2, y2):
        super().__init__()

        self.__vertex0 = (x0, y0)  # позиція другої відносно першої вершини
        self.__vertex1 = (x1, y1)  # позиція другої відносно першої вершини
        self.__vertex2 = (x2, y2)  # позиція третьої відносно першої вершини

    def draw(self):
        up()  # перестраховка, якщо пензлик був опущений

        pencolor(self.color)

        v0 = self.__vertex0
        v1 = self.__vertex1
        v2 = self.__vertex2

        setpos(self._calc_position(v0))
        down()
        setpos(self._calc_position(v1))
        setpos(self._calc_position(v2))
        setpos(self._calc_position(v0))

        up()


if __name__ == '__main__':
    t = Triangle(0, 0, 100, 0, 100, 100)
    print(t)

    reset()  # Ініціалізуємо режим малювання
    speed(1)
    # тут малюємо
    t.draw()

    t.position = (100, 150)
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
