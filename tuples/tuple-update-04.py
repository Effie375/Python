mytuple = ("Μήλο", "Μπανάνα", "Κεράσι")
mylist = list(mytuple)
mylist.remove("Μήλο")
mytuple = tuple(mylist)
print(mytuple)
