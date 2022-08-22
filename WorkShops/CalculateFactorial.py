from unittest import result

number = int(input("Enter The Number To Calculate Factorial: "))
result = 1

if number == 0:
    print("Result: 1")
elif number < 0:
    print("Invalid Number!!")
else:
    for num in range(1 , number + 1):
        result = result * num
    print("Result:" , result)
