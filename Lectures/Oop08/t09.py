class MyCollectionIterator:
    def __init__(self, container):
        self.collection = container
        self.current_position = 0

    def __next__(self):
        try:
            current = self.collection[self.current_position]
            self.current_position += 1
            return current
        except IndexError:
            raise StopIteration

class MyCollection:
    def __init__(self, *elems):
        self.__container = list(elems)

    def __str__(self):
        return f"MyCollection: {self.__container}"

    def __iter__(self):
        return MyCollectionIterator(self.__container)


if __name__ == '__main__':
    collection = MyCollection(2, 3, 4, 5, 6)
    print(collection)

    for i in collection:
        print(i)
    # print(*collection)