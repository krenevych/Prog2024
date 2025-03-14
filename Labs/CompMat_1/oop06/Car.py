from turtle import *  # Підключаємо модуль turtle

from Labs.CompMat_1.oop06.Figure import Figure
from Labs.CompMat_1.oop06.Rectangle import Rectangle
from Labs.CompMat_1.oop06.Triangle import Triangle


# class Car(Figure):
#     def __init__(self, *parts):
#         super().__init__()
#
#         self._parts: list[Figure] = list(parts)
#
#
#     def draw(self):
#
#         for part in self._parts:
#             part.draw()


if __name__ == '__main__':

    cabine = Triangle(200, 0, 100, 50)
    cabine.color = "yellow"
    cabine.position = (100, 150)
    cabine.draw()

    body = Rectangle(300, 100)
    body.position = (0, 50)
    body.color = "blue"
    body.draw()

    wheel1 = Rectangle(50, 50)
    wheel1.position = (50, 0)
    wheel1.color = "red"
    wheel1.draw()

    wheel2 = Rectangle(50, 50)
    wheel2.position = (150, 0)
    wheel2.color = "green"
    wheel2.draw()

    # car = Car(cabine, body, wheel1, wheel2)

    # car.draw()

    mainloop()       # Затримуємо вікно на екрані

