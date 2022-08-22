setA = {1,2,3,4,5}
setB = {2,4,5,6,7}

print(setA - setB)      # This time, display variable on the screen in setA but not in setB.
print(setA.difference(setB))

print(setA ^ setB)      # Displays just only variables that are unique to each other.
print(setA.symmetric_difference(setB))