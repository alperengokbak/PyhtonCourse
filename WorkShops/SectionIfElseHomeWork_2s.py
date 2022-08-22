num1 = 25
num2 = 18
num3 = 30

if num1 > num2 and num1 > num3:
    print("The biggest number is" , num1)
elif num2 > num1 and num2 > num3:
    print("The biggest number is" , num2)
elif num3 > num1 and num3 > num2:
    print("The biggest number is" , num3)

if num1 > num2 and num1 > num3:
    if num2 > num3:
        print("The smallest number is" , num3)
    else:
        print("The smallest number is" , num2)

elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print("The smallest number is" , num3)
    else:
        print("The smallest number is" , num1)

elif num3 > num1 and num3 > num2:
    if num1 > num2:
        print("The smallest number is" , num2)
    else:
        print("The smallest number is" , num1)