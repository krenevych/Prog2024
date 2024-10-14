
def table(xs, f):
    for x in xs:
        f_x = f(x)
        print(f"f({x})= {f_x}")


# def sqr(x):
#     return x * x

#
# def cubic(x):
#     return x ** 3


# table((0, 1, 2, 3, 4), sqr)
table((0, 1, 2, 3, 4), lambda x : x ** 3)

# a = 3
# b = 4
# c = a + b
# c = 3 + 4
