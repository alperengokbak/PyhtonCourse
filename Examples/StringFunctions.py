firstString = "Welcome to Germany!!"
secondString = "WeLcOmE tO gErMaNy"

if(firstString.upper() == secondString.upper()):
    print("Both of them are same!")
else:
    print("They are not same!")

#Substring Function
message = "Hello World"
print(message[6:11])    #This expression mean is, display from 6 to 11.
print(message[6:])    #This time, display from 6 at the end.
print(message[:6])    #Display at the starting to 6.

#Lenght(len) Function
print(len(message))    #This function shows us how many include char in char list.

#Lower Upper
print(message.upper())
print(message.lower())

#Replace Function
print(message.replace("H","s"))
print(message)
message = message.replace("H","s")    #If we would not change the expression in print function. This char always show changed variable.
print(message)

#Split and Strip
info = "Alperen Gökbak 23 Izmir"
print(info.split(" ")[1])   #Split keyword split a whole expression when see the space char.

#Input
name = input("Name ?")
number = input("Enter number: ")
result = int(number) + 10
print("Result: " , result)