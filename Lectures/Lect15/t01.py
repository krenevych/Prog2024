# серед заданого набору чисел знайти ті, які є простими
import random
import Lectures.Lect08.t02 as p

# from Lectures.Lect08.t02 import is_prime
# import Lectures.Lect08.t02

lst = [random.randint(0, 100) for i in range(10)]
# lst.append(29)
print(lst)

for el in lst:
    if p.is_prime(el):
        print(el)
