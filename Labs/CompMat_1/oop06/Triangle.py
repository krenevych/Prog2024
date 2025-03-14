import math

from Labs.CompMat_1.oop06.Figure import Figure
from turtle import * # Підключаємо модуль turtle

class Triangle(Figure):
    def __init__(self, *p):
        super().__init__()

        if len(p) == 6:
            self.__vertex0 = (p[0], p[1])  # позиція третьої відносно першої вершини
            self.__vertex1 = (p[2], p[3])  # позиція другої відносно першої вершини
            self.__vertex2 = (p[4], p[5])  # позиція третьої відносно першої вершини
        elif len(p) == 4:
            self.__vertex0 = (0, 0)  # позиція третьої відносно першої вершини
            self.__vertex1 = (p[0], p[1])  # позиція другої відносно першої вершини
            self.__vertex2 = (p[2], p[3])  # позиція третьої відносно першої вершини
        else:
            raise ValueError("Triangle: incorrect creation parameters")

    def draw(self):
        pencolor(self.color)
        up() # перестраховка, якщо пензлик був опущений

        v0 = self._calc_position(self.__vertex0)
        v1 = self._calc_position(self.__vertex1)
        v2 = self._calc_position(self.__vertex2)

        setpos(v0)
        down()
        setpos(v1)
        setpos(v2)
        setpos(v0)
        up()


if __name__ == '__main__':
    # t = Triangle(100, 0, 100, 100)
    # print(t)
    #
    # reset()  # Ініціалізуємо режим малювання
    # speed(1)
    # # тут малюємо
    # t.draw()
    #
    # # t.position = (100, 150)
    # # t.scale = (2, 2)
    # t.rotation = math.radians(30)
    # t.color = "blue"
    # t.pivot = (50, 30)
    # t.draw()
    #
    # # t.position = (100, 150)
    # t.scale = (2, 2)
    # t.rotation = math.radians(45)
    # t.color = "red"
    # t.pivot = (100, 100)
    # t.draw()

    cabine = Triangle(200, 0, 100, 100)
    cabine.color = "yellow"
    # cabine.position = (100, 150)
    cabine.draw()

    mainloop()       # Затримуємо вікно на екрані
