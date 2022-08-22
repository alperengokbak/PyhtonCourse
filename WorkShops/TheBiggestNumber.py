number1 = int(input("Enter The Number1: "))
number2 = int(input("Enter The Number2: "))
number3 = int(input("Enter The Number3: "))

if (number1 >= number2) & (number1 >= number3):
    print("The Biggest Number Is " + str(number1))
elif (number2 >= number1) & (number2 >= number3):
    print("The Biggest Number Is " + str(number2))
else:
    print("The Biggest Number Is " + str(number3))