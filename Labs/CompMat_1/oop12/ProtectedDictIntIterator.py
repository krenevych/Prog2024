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
