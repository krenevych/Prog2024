
try:
    f = open("input2.txt")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("File not found")