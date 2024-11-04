import shelve

d = shelve.open('t03_data')

d["Hello"] = "World"
d["hello"] = "world"
d["mech-mat"] = "forever"
d["specialities"] = ["математика", "статистика", "компʼютерна математика"]

for key, value in d.items():
    print(key, value)

d.close()
