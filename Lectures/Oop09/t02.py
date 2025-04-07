# 1 1 2 6 24 120
# 0 1 2 3 4    5

# def fact(n):
#     i = 0
#     f = 1
#     while i < n:
#         i += 1
#         f *= i
#     return f

def fact(n):
    i = 0
    f = 1
    yield f, "нульовий член послідовності"
    while i < n:
        i += 1
        f *= i
        yield f, f"{i}-й член послідовності"
        # return f - породжує StopIteration
    # return None - завжди присутнє, якщо ми не визначили явно
    # у випадку генераторів породжує неявно StopIteration


for f in fact(5):
    print(*f)

# print(fact(5))
# print(fact(0))
# print(fact(1))
