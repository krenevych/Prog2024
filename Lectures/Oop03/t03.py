from copy import copy, deepcopy

from Lectures.Oop03.t02 import Triangle


class Tetrahedron:
    def __init__(self, t1: Triangle, t2: Triangle):
        self.t1 = t1
        self.t2 = t2

    def print(self):
        print(f"Tetrahedron: {self}")
        self.t1.print()
        self.t2.print()


if __name__ == '__main__':
    tetrahedron = Tetrahedron(
        Triangle(3, 4, 5),
        Triangle(4, 4, 4)
    )

    print("==== tetrahedron ==== ")
    tetrahedron.print()

    tetrahedron2 = deepcopy(tetrahedron)

    print("==== tetrahedron2 ==== ")
    tetrahedron2.print()

    tetrahedron2.t1.c = 100500

    print("Після зміни: ")
    print("==== tetrahedron ==== ")
    tetrahedron.print()

    print("==== tetrahedron2 ==== ")
    tetrahedron2.print()





