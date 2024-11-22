# функцію для max з двох чисел

def max2(a, b):
    if a > b:
        return a
    else:
        return b

# функцію для max з трьох чисел
def max3(a, b, c):
    return max2(max2(a, b), c)

if __name__ == '__main__':
    # print(max2(45, 67))

    max_3 = max3(2, 5, 4)

    print(max_3)
