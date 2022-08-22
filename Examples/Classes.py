from ast import Mult

# %% Basics
class MathsProblem:
    def __init__(self , number1 , number2):
        self.number1 = number1
        self.number2 = number2

    def addition(self):     # You have to write "self" command. (Bellekten oluşan nesneye karşılık gelen bir nesne ile geliyor.)
        return self.number1 + self.number2

    def substraction(self):
        return self.number1 - self.number2

    def multiplication(self):
        return self.number1 * self.number2

    def division(self):
        return self.number1 / self.number2

maths = MathsProblem(50 , 10)
maths2 = MathsProblem(2 , 15)
print("Totally: " + str(maths2.addition()))

# %% Property

class Person(object):
    def __init__(self , firstName , lastName , age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

person = Person("Emine" , "Timur" , 22)
print(person.firstName , person.lastName , person.age)

# Inheritance
class Worker(Person):
    def __init__(self , firstName , lastName , age , salary):
        self.salary = salary
        super().__init__(firstName , lastName , age)    # We have to write "Mother Class" variable inside of "super()" function.

class Customer(Person):
    def __init__(self , creditCardNumber):
        self.creditCardNumber = creditCardNumber

emine = Worker("Emine" , "Timurr" , 22 , 20000)
print(emine.firstName , emine.lastName , emine.age , emine.salary)

# %%
