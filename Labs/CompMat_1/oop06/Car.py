import math
from turtle import mainloop

from Labs.CompMat_1.oop06.Figure import Figure
from Labs.CompMat_1.oop06.Rectangle import Rectangle
from Labs.CompMat_1.oop06.Triangle import Triangle


class Car(Figure):

    def __init__(self, *car_parts):
        super().__init__()

        self.parts: list[Figure] = list(car_parts)

    def draw(self):
        for part in self.parts:
            part.pivot = self.pivot
            part.position = self.position
            part.color = self.color
            part.rotation = self.rotation
            part.scale = self.scale
            part.draw()

if __name__ == '__main__':


    pivot = Rectangle(-5, -5, 5, 5)
    pivot.color = "red"
    pivot.draw()

    pivot_pos = (100, 50)
    pivot.position = pivot_pos
    pivot.color = "green"
    pivot.draw()

    body = Rectangle(-100, 50, 100, 150)
    wheel = Rectangle(-100, 0, -50, 50)
    wheel2 = Rectangle(50, 0, 100, 50)
    roof = Triangle(-100, 150, 100, 150, -50, 200)


    car = Car(body, wheel, wheel2, roof)
    car.draw()

    # car.position = (100, -200)
    car.color = "blue"
    car.pivot = pivot_pos
    car.rotation = math.radians(30)
    # car.scale = (2, 2)
    car.draw()

    # ==============
    pivot_pos = (-50, 200)
    pivot.position = pivot_pos
    pivot.draw()

    car.color = "green"
    car.pivot = pivot_pos
    car.draw()

    mainloop()       # Затримуємо вікно на екрані