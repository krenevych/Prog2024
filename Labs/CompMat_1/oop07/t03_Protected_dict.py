
class ProtectedDictInt(dict):

    def __setitem__(self, key, value):
        if type(key) != int:
            raise ValueError("Ключ має бути цілого типу")

        if key in self:
            raise ValueError("Такий ключ вже є у словнику")

        # self[key] = value  # = self.__setitem__(key, value)
        super().__setitem__(key, value)

    def __getitem__(self, key):  # self[key]
        if key in self:
            print(f"для ключа {key} такий елемент буде {super().__getitem__(key)}")
            return super().__getitem__(key)
        else:
            print(f"ключ {key} відсутній у словнику")
            return None

    def __add__(self, other : (dict, tuple, list)):
        assert isinstance(other, (dict, ProtectedDictInt, tuple, list))

        res = ProtectedDictInt()
        for k, v in self.items():
            res[k] = v
        if isinstance(other, dict):
            for k, v in other.items():
                res[k] = v
        elif isinstance(other, (tuple, list)):
            if len(other) == 2:
                res[other[0]] = other[1]
            else:
                raise ValueError("Права частина має містити рівно два числа")


        return res

    def __sub__(self, other):
        assert isinstance(other, int)
        res = ProtectedDictInt()
        for k, v in self.items():
            if k != other:
                res[k] = v
        return res


if __name__ == '__main__':
    p = ProtectedDictInt()
    p[4] = "Hello"
    print(p)
    # p[4] = "World" # виключення, бо змінювати не можна
    # print(p)
    # p["Hello"] = "World" # виключення, бо ключ не ціле
    # print(p)

    # p.update({"hello": "world"})
    # print(p)
    # print(4 in p)
    # print(len(p))
    # print(p[4])
    # print(p[4444])

    p1 = p + (5, 123)
    print(p1)

    p2 = p1 + {6: 1234, 90: 6554}
    print(p2)
    #
    p3 = ProtectedDictInt()
    p3[1] = 111
    p3[2] = 112
    # print(p2)
    #
    p4 = p2 + p3
    print(p4)

    p5 = p4 - 2
    print(p5)
