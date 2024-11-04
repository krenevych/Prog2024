import pickle

f = open("damp.bin", "rb")

loaded_obj = pickle.load(f)

f.close()

print(loaded_obj)