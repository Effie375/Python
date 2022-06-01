f = open("demofile.txt", "a")
f.write("Καζή Ευστρατία")
f.close()

f = open("demofile.txt", "r")
print(f.read())
