n = 110011

dec_n = 0
pow2 = 1
while n > 0:
    d = n % 10
    dec_n = dec_n + d * pow2
    n = n // 10
    pow2 = pow2 * 2

print(dec_n)