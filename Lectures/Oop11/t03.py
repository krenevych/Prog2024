# Опишемо клас виключення для функції введення з клавіатури
# лише невід’ємних цілих чисел.

ERROR_NON_INTEGER = 0
ERROR_NON_POSITIVE_INTEGER = 1

class InputPositiveIntException(Exception):
    def __init__(self, message, code_error):
        super().__init__()
        self.message = message
        self.code_error = code_error

    def __str__(self):
        return str(self.message)


def input_positive_int(*args, **kwargs):
    s = input(*args, **kwargs)
    try:
        s = int(s)  # ось тут може бути проблема конвертації до int
        if s < 0:   # тут може бути проблема, що введене число відʼємне
            raise InputPositiveIntException(
                "Введене ціле число не є невідʼємним",
                ERROR_NON_POSITIVE_INTEGER
            )

        return s

    except ValueError:
        raise InputPositiveIntException(
            "Введене число не цілого типу",
            ERROR_NON_INTEGER
        )




if __name__ == '__main__':
    try:

        a = input_positive_int("Задайте ціле невідʼємне значення ")
        print(a, type(a))
    except InputPositiveIntException as er:
        # print(er)
        if er.code_error == ERROR_NON_INTEGER:
            print("Задано значення не цілого типу")
        elif er.code_error == ERROR_NON_POSITIVE_INTEGER:
            print("Задане значення хоч і цілого типу, проте відʼємне")