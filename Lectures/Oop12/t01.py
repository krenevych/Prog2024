from abc import ABCMeta, abstractmethod

# Інтерфейс
class Diagnosabe(metaclass=ABCMeta):
    @abstractmethod
    def diagnose(self):
        pass

# клас Транспорт
class Transport:
    def __init__(self, resource = 100_000):
        self.resource = resource
        self.current_mileage = 0

    def driving(self):
        self.current_mileage += 15_000

class Car(Transport, Diagnosabe):
    def diagnose(self):
        current = 100 - self.current_mileage / self.resource * 100
        if current < 20:
            print("Car: Подумайте про капітальний ремонт")
        else:
            print(f"Car: Лишилося {current}% ресурсу автомобіля")

# клас Істота
class Creature:
    def __init__(self):
        self.health = 100

    def pass_exam(self):
        self.health -= 20

    def take_vacation(self):
        self.health += 5

class Human(Creature, Diagnosabe):

    def diagnose(self):
        if self.health < 30:
            print("Human: Вам терміново треба подумати про здоровʼя та поїхати у відпустку!")
        else:
            print(f"Human: Ваше здоровʼя на рівні {self.health}%")


if __name__ == '__main__':
    car = Car()
    car.driving()
    car.driving()
    # print(f"{100 - car.current_mileage / car.resource * 100}%")

    human = Human()
    human.pass_exam()
    human.take_vacation()
    # print(f"{human.health}% ")

    lst = [car, human]  # тип всіх елементів у списку буде Diagnosabe, бо всі вони реалізовують інтерфейс Diagnosabe
    for entity in lst:
        entity.diagnose()

    for i in range(5):
        human.pass_exam()
        car.driving()




    print("===================")
    for entity in lst:
        entity.diagnose()


