tupleList = ("Miami" , "Los Angels" , (1,2,3))
list = ["Miami" , "Los Angels" , [1,2,3]]
#tupleList[1] = "New York" (You must not change the tuple's variable after created a tuple.)
list[1] = "Colorado"

tupleValue = ("Love" , )   # We have to put "," at the right of the last variable , if we want to see type of variable is tuple.
print(type(tupleValue))

print(tupleList[-2]) # "-2" meaning is start from last of tuple or list. Second one from right of tuple.
print(list[-2])

print(len(tupleList))
print(len(list))
print(type(tupleList))
print(type(list))
print(tupleList)
print(list)
