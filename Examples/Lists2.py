myCities = ["Los Angels" , "New York" , "Washington"]
myCities2 = (("Miami", "Boston" , "New Zeland"))

#myCities.clear()    #This expression is clearing the whole list.

findNumber = myCities.count("Los Angels")   #This expression counts how many "Miami" inside of the list.
findIndex = myCities.index("New York")   #This expression shows which index include the "Boston"'s index.
removeIndex = myCities.pop(1)   #This expression removes index which you write between the brackets.
insertIndex = myCities.insert(0 , "Amsterdam")
copyIndex = myCities.copy()
extendIndex = myCities.extend(myCities2)     #This expression extends two list in eachother.(Sıralamak)
sortIndex = myCities.sort()     #This expression sorts the list.

city = input("Enter The City: ")

print("Number Of " + city + " : " + str(findNumber))
print("Index of " + city + " : " + str(findIndex))
print(extendIndex)
