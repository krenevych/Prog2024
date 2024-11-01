n = int(input())
elements = [int(el) for el in input().split()]

d_freq = {}  # словник де ключ - число, а значення скільки разів це число зустрічається у списку
for el in elements:
    d_freq[el] = elements.count(el)

for el, val in d_freq.items():
    if val == 1:
        elements.remove(el)
    else:
        for i in range(val - 1):
            elements.remove(el)

print(*elements)
# print(d_freq)