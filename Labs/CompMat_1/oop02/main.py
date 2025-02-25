from Labs.CompMat_1.oop02.QuadraticEquation import QuadraticEquation

equations = [] # буде містити список всіх рівнянь прочитаних з файлу
with open("input01.txt") as f:
    for line in f:
        try:
            a, b, c = [int(elem) for elem in line.split()]
            equations.append(QuadraticEquation(a, b, c))
        except ValueError:
            pass


for eq in equations:
    print(eq)
    print(eq.solve())
