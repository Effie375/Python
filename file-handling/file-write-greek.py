f = open("demo\\demofile.txt", "w", encoding='utf-8')
f.write("Καζή Ευστρατία")
f.close()

f = open("demo\\demofile.txt", "r", encoding='utf-8')
print(f.read())
