class ProtectedDictIntIterator:
    def __init__(self, collection: dict):
        self.__collection = collection
        self.__keys = list(collection.keys())
        self.__current = 0


    def __next__(self):
        try:
            key = self.__keys[self.__current]
            val = self.__collection[key]
            self.__current += 1
            return key, val
        except IndexError:
            raise StopIteration



class ProtectedDictInt:

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

    def __iter__(self):
        return ProtectedDictIntIterator(self.__inner_dict)

if __name__ == '__main__':

    p = ProtectedDictInt()
    p[4] = "Hello"
    p[14] = "World"
    p[123] = 123
    print(p)

    for i in p:
        print(i)

    print(*p)

