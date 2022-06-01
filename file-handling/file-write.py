f = open("demofile.txt", "w")
f.write("Καζή Ευστρατία")
f.close()

f = open("demofile.txt", "r")
print(f.read())
