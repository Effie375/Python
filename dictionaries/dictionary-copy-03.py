thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "years": [1964, 1983, 2000]
}

# Shallow copy
mydict = thisdict.copy()

thisdict["years"][2] = 2022

print(mydict)
