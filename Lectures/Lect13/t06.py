import os

print(os.getcwd())

print(os.listdir())
if os.path.exists("to_remove"):
    os.remove("to_remove")

print(os.listdir())

