suma = 0
with open("random_integers.txt") as f:
    for line in f:
        nums = [int(el) for el in line.split()]
        suma += sum(nums)

print(suma)