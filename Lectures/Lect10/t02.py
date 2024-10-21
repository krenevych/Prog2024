# 1 1 2 6 24  120
# 0 1 2 3 4   5    6 7 8 9

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

############ main #########
print(fact(5))
