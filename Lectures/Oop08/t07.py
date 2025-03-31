class MyCollection:
    def __init__(self, *elems):
        self.container = list(elems)

    def __str__(self):
        return f"MyCollection: {self.container}"


if __name__ == '__main__':
    collection = MyCollection(2, 3, 4, 5, 6)
    print(collection)

    for i in collection:
        print(i)