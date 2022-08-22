# List, Tuple, Set Summarize
# "{}" that brackets represents SETS.
# "[]" and "(())" brackets represents LISTS.
# "()" brackets represents TUPLES.
from this import d


set1 = {1,2,3,4,5}
set2 = {2,5,6,7,}
list1 = [1,2,3,4,5]
tuple1 = (1,2,3,4,5)

print(type(set1))
print(type(set2))
print(type(list1))
print(type(tuple1))

# If, Ifelse, Else keywords Summarize
if len(set1) > len(set2):
    print("These are not same size.")
else:
    print("These are same size.")

# For Loops Summarize
for number in set1:
    print(number)

# Function Summarize(def)
def passports():
    users = ["Alperen" , "Gokbak" , "Turkish" , 21]
    for information in users:
        print(information)
passports()

# Set Union Summarize
print(set1.union(set2))
print(set1 | set2)

# Set Intersection Summarize
print(set1 & set2)
print(set1.intersection(set2))

# Set Difference Summarize
print(set1 - set2)
print(set1.difference(set2))

# Set Symmetric Summarize
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

# Dictionary Summarize
dictionary1 = {"Book" : "Kitap" , "Car" : "Araba" , "Destiny" : "Kader"}
print(dictionary1)
del dictionary1["Car"]
print(dictionary1)
print(dictionary1["Book"])

dictionary2 = dict(Book = "Kitap" , Car = "Araba" , Destiny = "Kader")
print(dictionary2)
dictionary2["Clap Clap!"] = "Alkışlamak"
print(dictionary2)
del dictionary2["Book"]
print(dictionary2)

#For Loops
dates = [18 , 25 , 30 , 9 , 7]

for date in dates:
    if date > 20:
        print(date)
    elif date == 20:
        print(date)
    else:
        print("NULL!")

# While Loops
number1 = 1
number2 = 1
result = 0

while (number1 + number2) <= 20:
    result = number1 + number2
    if number1 == number2:
        number2 = number2 + 1
    number1 = number1 + 1
    print(number1 , number2)
print(result)

# Range Function
for number in range(1 , 10):
    print(number)

for number in range(1 , 10 , 2):
    print(number)