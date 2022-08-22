# If you use one expression more than one. We can use the functions.

#%% Cell 1(Beginning)
from ast import Lambda


city = "Miami"
print(city.upper())
print(city.endswith("i"))  # That word is ending with letter between brackets.

#%% Cell2(Example)
def greets2(name = "Visitor" , surName = "Anonim"):   # Display "Visitor"(Default Value). If you dont assigment any variable for name.
    print("Hello " + name + "" + surName)

greets2("Emine")
greets2("")

#%% Cell3(Return Function)
def calculateFieldTriAngel(a , b):
    return a * b / 2
print(calculateFieldTriAngel(6 , 6))

#%% Cell4(Lambda Function)
calculateFieldTriAngel2 = lambda a , b : a * b / 2      # It have to just a line. That function like a return function.

print(calculateFieldTriAngel2(3 , 2))
print(type(calculateFieldTriAngel2))

x = calculateFieldTriAngel2     # You can assigment funtion to variable. It's possible for pyhton.
print(x(6 , 5))