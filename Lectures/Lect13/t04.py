import shelve

d = shelve.open('t03_data')

d['newdata'] = "new_data"

for key, value in d.items():
    print(key, value)



d.close()
