import random

# Generate a list of 10 random integers between 1 and 100
random_integers = [random.randint(1, 100) for _ in range(500)]

with open('random_integers.txt', 'w') as f:
    print(*random_integers, file=f)