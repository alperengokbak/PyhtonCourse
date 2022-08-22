import basicCalculatorMainFunc as cal

print("Welcome To Our Calculator Machine!!")
cal.menu()
selection = str(input())
    
if selection == '0':
    quit()
elif selection == '1':
    number1 = int(input("Enter The Number1: "))
    number2 = int(input("Enter The Number2: "))
    print("Totally: " + str(cal.addition(number1 , number2)))
elif selection == '2':
    number1 = int(input("Enter The Number1: "))
    number2 = int(input("Enter The Number2: "))
    print("Totally: " + str(cal.substraction(number1 , number2)))
elif selection == '3':
    number1 = int(input("Enter The Number1: "))
    number2 = int(input("Enter The Number2: "))
    print("Totally: " + str(cal.multiplication(number1 , number2)))
elif selection == '4':
    number1 = int(input("Enter The Number1: "))
    number2 = int(input("Enter The Number2: "))
    print("Totally: " + str(cal.division(number1 , number2)))
else:
    print("Invalid Number!!") 