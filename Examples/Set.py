setExample = {"Miami" , "California" , 1 , 2 , 3 , "Miami"}
setExample2 = set("Ali")
tupleExample = ("Miami" , "Miami")
listExample = ["Miami" , "Rome"]

print(type(tupleExample))
print(type(setExample))   # You must not display two same variable in sets.
print(type(listExample))
print(type(setExample2))

print(setExample)   # There is not any sorting. Python sort in yourself algorithm.

for city in setExample:
    print(city)

print("Maiami" in setExample)    # If there is "Miami" in that set. This expression returning true.

if "Miami" in setExample:
    print("There is Miami in that set.")
    setExample.add("Berlin")
    setExample.update(["EA" , 3008])     # Python allows add more than one variable at the same time.
    print(setExample)

    print(len(setExample))
    setExample.remove(1)    # Python provides to remove variable in the set.
    print(setExample)

    setExample.discard(1)   # That keyword does not display error. If you trying to remove same variable at the before time.

    del setExample      # Directly delete whole variable and set.
    print(setExample)