import math
from turtle import * # Підключаємо модуль turtle


class Triangle:

    def __init__(self, x1, y1, x2, y2):
        self.__position = (0, 0)   # абсолютна позиція першої вершини
        self.__vertex1 = (x1, y1)  # позиція другої відносно першої вершини
        self.__vertex2 = (x2, y2)  # позиція третьої відносно першої вершини
        self.__rotation = 0        # кут повороту в радіанах
        self.__scale = (1, 1)      # масштаб фігури
        self.__pivot = (0, 0)      # опорна точка

        self.__color = "black"     # колір трикутника за промовчанням

    @property
    def rotation(self):    # значення в радіанах
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation):    # значення в радіанах
        self.__rotation = rotation

    @property
    def scale(self):    # значення в радіанах
        return self.__scale

    @scale.setter
    def scale(self, scale):    # значення в радіанах
        self.__scale = scale

    @property
    def pivot(self):
        return self.__pivot

    @pivot.setter
    def pivot(self, pivot):
        self.__pivot = pivot

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, pos):
        assert isinstance(pos, (tuple, list)) and len(pos) == 2
        self.__position = pos

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        # має бути перевірка, чи параметр color дійсно color
        self.__color = color

    def __str__(self):
        return f"Triangle: {self.__position, self.__vertex1, self.__vertex2}"

    def __calc_position(self, vertex):
        x, y = vertex[0], vertex[1]

        x, y = x - self.__pivot[0], y - self.__pivot[1]  # зміщуємо вершини трикутника, так, щоб точка pivot збіглася з початком координат

        x, y = self.scale[0] * x, self.__scale[1] * y # розтягуємо

        # обертання
        cos_phi = math.cos(self.__rotation)
        sin_phi = math.sin(self.__rotation)
        x, y = cos_phi * x - sin_phi * y, sin_phi * x + cos_phi * y

        x, y = self.__position[0] + x, self.__position[1] + y  # перенос в позицію self.__position

        x, y = x + self.__pivot[0], y + self.__pivot[1]  # повертаємо трикутник назад

        return  x, y

    def draw(self):
        up() # перестраховка, якщо пензлик був опущений

        goto(self.__calc_position(self.__position))
        pencolor(self.__color)

        down()

        # зміщені координати для vertex1
        # x, y = self.__position[0] + self.__vertex1[0], self.__position[1] + self.__vertex1[1]
        x, y = self.__calc_position(self.__vertex1)
        setpos(x, y)

        # зміщені координати для vertex1
        # x, y = self.__position[0] + self.__vertex2[0], self.__position[1] + self.__vertex2[1]
        x, y = self.__calc_position(self.__vertex2)
        setpos(x, y)

        setpos(self.__calc_position(self.__position))
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
