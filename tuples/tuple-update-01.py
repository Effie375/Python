mytuple = ("Μήλο", "Μπανάνα", "Κεράσι")
mylist = list(mytuple)
mylist[1] = "Αχλάδι"
mytuple = tuple(mylist)
print(mytuple)
