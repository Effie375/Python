class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Το όνομα μου είναι " + abc.name)

p1 = Person("Ευστρατία", 20)
p1.myfunc()
