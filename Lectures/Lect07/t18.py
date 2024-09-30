https = "www.mechmat.knu.ua"
parts = https.split(".")
print(parts)


newhttps = https.replace(".", "_")
print(newhttps)

newhttps2 = "_____".join(parts)
print(newhttps2)
