class Pet:
    def __init__(self, name):
        self._name = name

    def voice(self):
        print(f"I'm base class, I don't know what to say!")

    @property
    def name(self):
        return self._name

class Cat(Pet):

    def voice(self):
        print(f"Cat {self._name} says Miu-miu!!!")

class Dog(Pet):
    def voice(self):
        print(f"Dog {self._name} says Bau-bau!!!")

if __name__ == '__main__':
    p = Pet("Базовий")
    p.voice()

    c = Cat("Кабан")
    c.voice()

    d = Dog("Кулька")
    d.voice()
