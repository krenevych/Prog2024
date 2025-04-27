from Labs.CompMat_1.oop12.ProtectedDictException import ProtectedDictIntError, ProtectedDictKeyAlreadyExists, \
    ProtectedDictError
from Labs.CompMat_1.oop12.ProtectedDictIntIterator import ProtectedDictIntIterator


class ProtectedDictInt:

    def __init__(self):
        self.__inner_dict = {} # звичайний словник

    def __setitem__(self, key, value):
        if type(key) != int:
            # raise ValueError("Ключ має бути цілого типу")
            raise ProtectedDictIntError(
                key,
                value
            )

        if key in self.__inner_dict:
            # raise ValueError("Такий ключ вже є у словнику")
            raise ProtectedDictKeyAlreadyExists(
                key,
                value
            )
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

    try:
        p[14] = "World"
        # p[14] = "Hello"
        p["15"] = "World"
        p[4] = "Hello"
        p[123] = "123"
        print(p)

    # except ProtectedDictError as er:
    #     print("something went wrong")
    #     print(type(er))
    #
    #     er_type = type(er)
    #     er_check = isinstance(er, ProtectedDictIntError)
    #
    #     if isinstance(er, ProtectedDictKeyAlreadyExists):
    #         print("Ключ вже є в словнику")
    #     # elif isinstance(er, ProtectedDictInt):
    #     elif isinstance(er, ProtectedDictIntError):
    #         print("Ключ не цілиий")

    except ProtectedDictKeyAlreadyExists as er:
        print(type(er), er)
    except ProtectedDictIntError as er:
        print(type(er), er)
        try:
            key = int(er.key)
            p[key] = er.value
        except ValueError:
            pass

    for i in p:
        print(i)


