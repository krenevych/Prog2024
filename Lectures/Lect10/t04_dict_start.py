d = {
    "Hello": "World",
    "first": 1,
    2: "second"
}

print(d)
print(d["Hello"])
d["Hello"] = "hello"
print(d)
d["python"] = "Best of the best"
print(d)
del d["python"]
print(d)

# print(d[123])  # породить помилку, бо елементу з таким ключем немає в словнику

for key in d:
    print(key)

