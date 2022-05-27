try:
    f = open("myfile.txt")
    try:
        f.write("Kazi Efstratia")
    except:
        print("Κάτι πήγε στραβά κατά το γράψιμο του αρχείου!")
    finally:
        f.close()
except:
    print("Κάτι πήγε στραβά κατά το άνοιγμα του αρχείου!")