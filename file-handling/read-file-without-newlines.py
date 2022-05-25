f = open("demofile.txt", "r")
print([line.rstrip() for line in f.readlines()])
f.close()
