import math
from turtle import * # Підключаємо модуль turtle

# абстрактний клас фігура, що містить властивості та поведінку спільні для всіх типів фігур
class Figure:

    def __init__(self):
        self.__position = (0, 0)   # абсолютна позиція першої вершини
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
        return f"Figure"

    def _calc_position(self, vertex):
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

    # просто задекларую, що такий метод існує і може бути використаний програмістом,
    # але його реалізацію забезпечимо в конкретних нащадках
    # пізніше, використовуючи механізм абстрактних класів, ми забезпечимо гарантію того, що
    # програміст який буде реалізовувати відповідний нащадок, не забуде реалізувати цей метод
    def draw(self):
        pass


if __name__ == '__main__':
    t = Figure()

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
