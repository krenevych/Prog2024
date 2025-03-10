class Wheel:

    def __init__(self, properties: str):
        self.properties = properties

    def __str__(self):
        return self.properties

class Car:
    def __init__(self, wheel: Wheel):
        self.wheel = wheel

    def drive(self):
        print("driving...")
        print(self.wheel)

    def __del__(self):
        print("Car is deleted")

if __name__ == '__main__':
    w = Wheel("17'', forged, Michellen")
    c = Car(w)
    c.drive()

    del c
    # c.drive()
    print(w)
