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
        try:
            return self.__elements[key]
        except IndexError:
            return None

    def __setitem__(self, key, value):
        try:
            self.__elements[key] = value
        except IndexError:
            self.__elements.append(value)


# lst = [1, 2, 3]
# print(lst)
#
# # lst[666] = 2  # [1, 2, 3, 666]
#
# print(lst)
#
# print(lst[666])  # None
if __name__ == '__main__':
    c = Collection(3, 4, 5, 6)
    print(c)
    print(f"{len(c)=}")
    print(f"{c[2]=}")
    print(f"{c[666]=}")

    c[2] = 777   # c.__setitem__(2, 777)
    print(f"{c=}")

    c[888] = 999
    print(f"{c=}")

