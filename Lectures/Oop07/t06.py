class Collection:

    def __init__(self, *initial_set_of_values):
        self.__elements = list(initial_set_of_values)

    def __str__(self):
        return str(self.__elements)

    def __repr__(self):
        return str(self)

    def __len__(self):
        return len(self.__elements)

    def __getitem__(self, key):
        return self.__elements[key] if key < len(self) else None

    def __setitem__(self, key, value):
        if key < len(self):
            self.__elements[key] = value
        else:
            self.__elements.append(value)

    def __contains__(self, item):
        return item in self.__elements

    def __delitem__(self, key):
        if key < len(self):
            self.__elements.pop(key)


if __name__ == '__main__':
    c = Collection(3, 4, 5, 6)
    print(c)

    # print(f"{c[2]=}")
    # print(f"{c[22]=}")
    #
    # c[2] = 777
    # print(c)
    # c[22] = 777
    # print(c)

    print(f"{3 in c=}")
    print(f"{33 in c=}")


    del c[1]
    print(c)

    del c[444]
    print(c)
