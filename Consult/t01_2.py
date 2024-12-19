def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False  # число не просте!!!
    return True


####### main ########

print(is_prime(1))  # False
print(is_prime(12)) # False
print(is_prime(13)) # True