class NewClass:
    def __init__(self):
        self.bar = None
        self.a = 100

    def foo(self):
        self.bar = "Hello"




a = NewClass()
# a.foo()
print(a.bar)