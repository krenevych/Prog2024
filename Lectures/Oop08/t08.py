lst = [1, 2, 3]

# it = iter(lst)
#
# print(it)

# nxt = next(it)
# print(nxt)
# nxt = next(it)
# print(nxt)
# nxt = next(it)
# print(nxt)
# nxt = next(it)
# print(nxt)

# for i in lst:
#     print(i)

it = iter(lst)
while True:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break
