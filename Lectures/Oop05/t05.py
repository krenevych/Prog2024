# композиція

class Wheel:

    def __init__(self, properties: str):
        self.properties = properties

    def __str__(self):
        return self.properties

class Car:
    def __init__(self):
        self.wheel = Wheel("17'', forged, Michellen")

    def drive(self):
        print("driving...")
        print(self.wheel)

    def __del__(self):
        print("Car is deleted")

if __name__ == '__main__':
    c = Car()
    c.drive()
    del c
    print(c.wheel)


