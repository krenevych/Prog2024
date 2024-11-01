
n = int(input())

# elements = set(input().split())
elements = {int(el) for el in input().split()}
print(elements)

print(len(elements))