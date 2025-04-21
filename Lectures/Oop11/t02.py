# Опишемо клас виключення для функції введення з клавіатури
# лише невід’ємних цілих чисел.

def input_positive_int(*args, **kwargs):
    s = input(*args, **kwargs)
    s = int(s)
    if s < 0:
        raise ValueError
    return s



if __name__ == '__main__':
    try:

        a = input_positive_int("Задайте ціле невідʼємне значення ")
        print(a, type(a))
    except ValueError:
        print("Введене значення не ціле або відʼємне")