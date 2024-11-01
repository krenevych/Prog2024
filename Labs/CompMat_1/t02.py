n = int(input())
elements = [int(el) for el in input().split()]

d_freq = {}  # словник де ключ - число, а значення скільки разів це число зустрічається у списку
for el in elements:
    d_freq[el] = elements.count(el)

# print(d_freq)
# print(max(d_freq.values()))

N_2 = n // 2
for el, val in d_freq.items():
    # print(el, val)
    if val > N_2:
        print(el)
        break
else:
    print(-1)