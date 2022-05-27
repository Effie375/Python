try:
    print(x)
except NameError:
    print("Η μεταβλητή x δεν έχει οριστεί.")
except:
    print("Κάτι άλλο πήγε στραβά.")
