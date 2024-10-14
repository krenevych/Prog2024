def convert_to_dec(n, k=10):  # за промовчанням система числення, з якої ми переводимо буде десяткова
    pow_k = 1
    converted = 0
    while n > 0:
        last = n % 10
        converted += last * pow_k
        pow_k *= k
        n = n // 10
    return converted

def convert_from_dec(n, k=10):  # за промовчанням система числення, з якої ми переводимо буде десяткова
    # це алгоритм ми отримати заміною k на 10 і 10 на k по всій функції
    pow_10 = 1
    converted = 0
    while n > 0:
        last = n % k  # last = n % 10
        converted += last * pow_10
        pow_10 *= 10 # pow_k *= k
        n = n // k  # n = n // 10
    return converted

def convert_from_dec_str(n, k=10):  # за промовчанням система числення, з якої ми переводимо буде десяткова
    # це алгоритм ми отримати заміною k на 10 і 10 на k по всій функції
    converted = ""  # рядок цифр
    while n > 0:
        last = n % k  # last = n % 10
        converted = str(last) + converted
        n = n // k  # n = n // 10
    return converted

######## main ###########

dec = convert_to_dec(256, 8)
print(dec)

oct = convert_from_dec_str(dec, 8)
print(oct)