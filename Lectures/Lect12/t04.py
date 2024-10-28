f = open("cat.txt", "rt")

print("===========")
s = f.read()
print(s)
print("===========")
f.seek(0)
s = f.read(10)
s = f.read()
print(s)
print("===========")

f.close()