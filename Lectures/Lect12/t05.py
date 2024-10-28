
f = open("cat2.txt")

s = f.readline()
# print(s)

# list_of_lines = f.readlines()
# print(list_of_lines)
for line in f:
    print(line)


f.close()