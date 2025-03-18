from Lectures.Oop06.BaseXerox import BaseXerox


class Xerox(BaseXerox):
    pass


class Scaner:
    def copy(self):
        print("Scaner: copying...")

# клас БагатоФункціональнийПристрій - нащадок двох класів Xerox, Scaner
class MFD(Xerox, Scaner):
    pass


if __name__ == '__main__':
    mfd = MFD()
    mfd.copy() # викликаючи цей метод, ми можемо подумати,
    # що викличеться метод успадкований з класу Scaner, бо він в зоні видимості