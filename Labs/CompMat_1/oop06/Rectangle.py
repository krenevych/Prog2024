import math

from Labs.CompMat_1.oop06.Figure import Figure
from turtle import * # Підключаємо модуль turtle

class Rectangle(Figure):

    def __init__(self, *p):
        super().__init__()

        # self.__vertex0 = (x0, y0)  # позиція другої відносно першої вершини
        # self.__vertex1 = (x1, y0)  # позиція другої відносно першої вершини
        # self.__vertex2 = (x1, y1)  # позиція другої відносно першої вершини
        # self.__vertex3 = (x0, y1)  # позиція протилежної діагоналі прямокутника

        if len(p) == 4:
            self.__vertex0 = (p[0], p[1])  # позиція третьої відносно першої вершини
            self.__vertex1 = (p[2], p[1])  # позиція другої відносно першої вершини
            self.__vertex2 = (p[2], p[3])  # позиція третьої відносно першої вершини
            self.__vertex3 = (p[0], p[3])  # позиція третьої відносно першої вершини
        elif len(p) == 2:
            self.__vertex0 = (0   , 0   )  # позиція третьої відносно першої вершини
            self.__vertex1 = (p[0], 0   )  # позиція другої відносно першої вершини
            self.__vertex2 = (p[0], p[1])  # позиція третьої відносно першої вершини
            self.__vertex3 = (0   , p[1])  # позиція третьої відносно першої вершини
        else:
            raise ValueError("Triangle: incorrect creation parameters")

    def draw(self):
        up()  # перестраховка, якщо пензлик був опущений

        pencolor(self.color)

        v0 = self._calc_position(self.__vertex0)
        v1 = self._calc_position(self.__vertex1)
        v2 = self._calc_position(self.__vertex2)
        v3 = self._calc_position(self.__vertex3)

        setpos(v0)
        down()
        setpos(v1)
        setpos(v2)
        setpos(v3)
        setpos(v0)

        up()


if __name__ == '__main__':
    t = Rectangle(100, 100, 200, 200)
    t2 = Rectangle(200, 100)

    reset()  # Ініціалізуємо режим малювання
    speed(1)
    # тут малюємо
    t.draw()
    t2.draw()

    # t.position = (100, 150)
    t.scale = (2, 1)
    t.rotation = math.radians(30)
    t.color = "blue"
    t.pivot = (100, 0)
    t.draw()
    #
    # # t.position = (100, 150)
    # # t.scale = (2, 2)
    # t.rotation = math.radians(45)
    # t.color = "red"
    # t.pivot = (100, 0)
    # t.draw()

    mainloop()       # Затримуємо вікно на екрані
