from audioop import lin2adpcm
from calendar import c
from operator import le


city = {1: "Miami" , 2: "California" , 3: "New York"}
library = {"Book" : "Harry Potter" , "Contry" : "USA" , "City" : "Miami"}
names = dict(Male = "Alperen" , Female = "Emine")       # You can define dictionary at the same time.
print(city)
print(names)

# You can find the variable what you want like this:
print(city[3])
print(library["Book"])

# You can update or change the variables.
city[1] = "Colorado"
library["Contry"] = "Canada"
print(city)
print(library)

# You can add variable in dictionary
library["Store"] = "D&R"
print(library)

names["Old"] = 23
print(names)

# You can delete the variable in dictionary
del(library["Store"])
print(library)

print(len(names))

