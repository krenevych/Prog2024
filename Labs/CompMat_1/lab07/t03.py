def gcd(n, m):
    if n < m:
        n, m = m, n

    while m > 0:
        n, m = m, n % m

    return n



#   n    m
#   15   12
#   15 % 12 = 3
#   12 % 3  = 0
#   3    0

###### main #######
print(gcd(3 * 5 * 7, 2 * 3 * 5 * 11))