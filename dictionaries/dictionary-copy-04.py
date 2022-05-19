from copy import deepcopy

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "years": [1964, 1983, 2000]
}

# Deep copy
mydict = deepcopy(thisdict)

thisdict["years"][2] = 2022

print(mydict)
