class BaseClass:
    def printHello(self):
        print("Hello")

    def printWorld(self):
        print("World")

class NewClass(BaseClass):

    def printHello(self):
        print("Hello from new class,", end=" ")

if __name__ == '__main__':
    print("From BaseClass")
    b = BaseClass()
    b.printHello()
    b.printWorld()

    print("From NewClass")
    n = NewClass()
    n.printHello()
    n.printWorld()