from turtle import * # Підключаємо модуль turtle


class Triangle:

    def __init__(self, x1, y1, x2, y2):
        self.position = (0, 0)   # абсолютна позиція першої вершини
        self.vertex1 = (x1, y1)  # позиція другої відносно першої вершини
        self.vertex2 = (x2, y2)  # позиція третьої відносно першої вершини

        self.color = "black"     # колір трикутника за промовчанням

    def __str__(self):
        return f"Triangle: {self.position, self.vertex1, self.vertex2}"

    def draw(self):
        up() # перестраховка, якщо пензлик був опущений

        goto(self.position)

        down()
        setpos(self.vertex1)
        setpos(self.vertex2)
        setpos(self.position)



        up()


if __name__ == '__main__':
    t = Triangle(100, 0, 100, 100)
    print(t)

    reset()  # Ініціалізуємо режим малювання
    speed(1)
    # тут малюємо
    t.draw()
    mainloop()       # Затримуємо вікно на екрані
