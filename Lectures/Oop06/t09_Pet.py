class Pet:
    def __init__(self, name):
        self._name = name

    def voice(self):
        print(f"I'm base class, I don't know what to say!")

    @property
    def name(self):
        return self._name

class Cat(Pet):

    def __init__(self, name, master):
        # super().__init__(name) # виклик конструктора базового класу - ОБОВʼЯЗКОВО!
        Pet.__init__(self, name) # виклик конструктора базового класу, з явним указанням батьківського класу.
        self.master_name = master

    def __str__(self):
        return f"{self.name}, {self.master_name}"

    def voice(self):
        print(f"Cat {self._name} says Miu-miu!!!")




if __name__ == '__main__':


    c = Cat("Кабан", "Артур")
    c.voice()
    print(c)

