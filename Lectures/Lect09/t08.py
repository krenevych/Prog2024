def suma(*args):
    res = 0
    for el in args:
        res += el

    return res


######### main ##############
a, b, c = 1, 3, 4
s = suma(5, 6, 2, a, b, c)
print(s)