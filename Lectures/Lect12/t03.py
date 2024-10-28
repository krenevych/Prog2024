f = open("cat.txt", "rt")

s = f.read(10)
print(s)

print(f.tell())

s = f.read(10)
print(s)
print(f.tell())

f.seek(30)
s = f.read(10)
print(s)

f.seek(0)
s = f.read(10)
print(s)




f.close()