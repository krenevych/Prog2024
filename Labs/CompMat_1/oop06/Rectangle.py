import math

from Labs.CompMat_1.oop06.Figure import Figure
from turtle import * # Підключаємо модуль turtle

class Rectangle(Figure):

    def __init__(self, x0, y0, x1, y1):
        super().__init__()

        self.__vertex0 = (x0, y0)   # позиція протилежної діагоналі прямокутника
        self.__vertex1 = (x1, y0)   # позиція протилежної діагоналі прямокутника
        self.__vertex2 = (x1, y1)   # позиція протилежної діагоналі прямокутника
        self.__vertex3 = (x0, y1)   # позиція протилежної діагоналі прямокутника

    def draw(self):
        up()  # перестраховка, якщо пензлик був опущений

        pencolor(self.color)

        v0 = self.__vertex0
        v1 = self.__vertex1
        v2 = self.__vertex2
        v3 = self.__vertex3

        setpos(self._calc_position(v0))
        down()
        setpos(self._calc_position(v1))
        setpos(self._calc_position(v2))
        setpos(self._calc_position(v3))
        setpos(self._calc_position(v0))

        up()


if __name__ == '__main__':
    t = Rectangle(0, 0, 200, 100)

    reset()  # Ініціалізуємо режим малювання
    speed(1)
    # тут малюємо
    t.draw()

    # t.position = (100, 150)
    # t.scale = (2, 2)
    t.rotation = math.radians(30)
    t.color = "blue"
    t.pivot = (-50, -50)
    t.draw()
    #
    # # t.position = (100, 150)
    # # t.scale = (2, 2)
    # t.rotation = math.radians(45)
    # t.color = "red"
    # t.pivot = (100, 0)
    # t.draw()

    mainloop()       # Затримуємо вікно на екрані
