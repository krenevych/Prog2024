class ProtectedDictInt:
    """
    5.2.1.	Опишіть клас ProtectedDictInt, що є словником у якому,
     ключами можуть бути лише цілі числа
     та заборонена операція зміни значення за ключем
     (крім випадку додавання нової пари ключ-значення).
     Перевантажте для цього класу оператор [] (квадратні дужки) у такий спосіб:
•	для запису – додавання нової пари ключ-значення.
•	для читання – повертає значення зі словника.



    """
    def __init__(self):
        self.__inner_dict = {} # звичайний словник

    def __setitem__(self, key, value):
        if type(key) != int:
            raise ValueError("Ключ має бути цілого типу")

        if key in self.__inner_dict:
            raise ValueError("Такий ключ вже є у словнику")

        self.__inner_dict[key] = value

    def __getitem__(self, key):
        return self.__inner_dict[key]

    def __str__(self):
        return str(self.__inner_dict)

    def __contains__(self, key):
        return key in self.__inner_dict

if __name__ == '__main__':
    # d = {}
    # d[4] = "Hello"
    # d["Hello"] = "World"
    # print(d)
    # d[4] = "World"
    # print(d)

    p = ProtectedDictInt()
    p[4] = "Hello"
    print(p)
    # p[4] = "World" # виключення, бо змінювати не можна
    # print(p)
    # p["Hello"] = "World" # виключення, бо ключ не ціле
    # print(p)

    # p.update({"hello": "world"})

    print(4 in p)
