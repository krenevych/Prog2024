import pickle


obj = {
    "Hello" : "World",
    "hello" : "world",
    "mech-mat" : "forever",
    "specialities": ["математика", "статистика", "компʼютерна математика"]
}

f = open('damp.bin', "wb")
pickle.dump(obj, f)
f.close()

