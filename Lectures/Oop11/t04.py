# Опишемо клас виключення для функції введення з клавіатури
# лише невід’ємних цілих чисел.

class InputPositiveIntException(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return str(self.message)

class InputPositiveIntExceptionIntError(InputPositiveIntException):
    # виключення, що введене значення не ціле число
    pass

class InputPositiveIntExceptionNonNegativeError(InputPositiveIntException):
    # виключення, що введене значення ціле, проте відʼємне
    pass

def input_positive_int(*args, **kwargs):
    s = input(*args, **kwargs)
    try:
        s = int(s)  # ось тут може бути проблема конвертації до int
        if s < 0:   # тут може бути проблема, що введене число відʼємне
            raise InputPositiveIntExceptionNonNegativeError(
                "Введене ціле число не є невідʼємним",
            )

        return s

    except ValueError:
        raise InputPositiveIntExceptionIntError(
            "Введене число не цілого типу",
        )




if __name__ == '__main__':
    try:

        a = input_positive_int("Задайте ціле невідʼємне значення ")
        print(a, type(a))
    # except InputPositiveIntException as er:
    #     print(er)
    #     print(type(er))
    except InputPositiveIntExceptionIntError:
        print("Введене значення не цілого типу ККККК")
    except InputPositiveIntExceptionNonNegativeError:
        print("Введене значення цілого типу, проте є відʼємним ЕЕЕЕЕ")
