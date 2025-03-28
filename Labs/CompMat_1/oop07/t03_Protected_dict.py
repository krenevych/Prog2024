class ProtectedDictInt(dict):

    def __setitem__(self, key, value):
        if type(key) != int:
            raise ValueError("Ключ має бути цілого типу")

        if key in self:
            raise ValueError("Такий ключ вже є у словнику")

        # self[key] = value  # = self.__setitem__(key, value)
        super().__setitem__(key, value)


if __name__ == '__main__':

    p = ProtectedDictInt()
    p[4] = "Hello"
    print(p)
    # p[4] = "World" # виключення, бо змінювати не можна
    # print(p)
    # p["Hello"] = "World" # виключення, бо ключ не ціле
    # print(p)

    p.update({"hello": "world"})
    print(p)