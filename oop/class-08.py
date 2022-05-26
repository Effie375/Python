class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Το όνομα μου είναι " + self.name)

p1 = Person("Ευστρατία", 20)

del p1

print(p1)
