class MyCollectionIterator:
    def __init__(self, container):
        self.collection = list(container)
        self.collection.sort()
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
    collection = MyCollection(2, 13, 1, 5, 3)

    for i in collection:
        print(i)
        print("===== Start j =====")
        for j in collection:
            print(j)
        print("===== Finish j ====")

    print(collection)
