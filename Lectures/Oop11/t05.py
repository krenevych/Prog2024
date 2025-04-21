from abc import abstractmethod, ABCMeta


class Pet(metaclass = ABCMeta):
    def __init__(self, name):
        self.name = name

    # абстрактний (або чистий віртуальний) метод
    @abstractmethod
    def voice(self):
        pass


class Cat(Pet):

    def voice(self):
        print("Miu-miu!")


if __name__ == '__main__':
    # p = Pet("Pet")
    # print(p.name)
    # p.voice()

    c = Cat("Kuzya")
    print(c.name)
    c.voice()