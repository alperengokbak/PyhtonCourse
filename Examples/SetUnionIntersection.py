# Set union works like that, If you have two list and there are same variable each lists, display just one time.
setA = {1,2,3,4,5}
setB = {2,4,5,6,7}

print(setA | setB)      # You should use that rule to union both of sets.
print(setA.union(setB)) # Both of type is useful to union sets each others.

print(setA & setB)      # That keyword(Interseciton) displays same variable inside of both sets.
print(setA.intersection(setB))  # That pattern is displaying same result as well as top line.