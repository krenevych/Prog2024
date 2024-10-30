def inv(d) -> str:
    if d <= 9:
        return str(d)
    else:
        return str(d % 10) + inv(d // 10)

def convert(n, b) -> str:
    if n < b:
        return str(n)
    else:
        return  convert(n // b, b) + str(n % b)

# print(inv(2345))
print(convert(256, 8))
