class Class4: pass
class Class5: pass
class Class6: pass
class Class3(Class6): pass
class Class2(Class4, Class5): pass
class Class1(Class2, Class3): pass


print(Class1.__mro__)
