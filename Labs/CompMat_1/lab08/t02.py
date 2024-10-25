def mult(n, m):
    if n == 0 or m == 0:
        return 0
    elif m > n:
        return mult(m, n)
    else:
        return mult(n, m-1) + n

###### main ###########

print(mult(3, 4))
