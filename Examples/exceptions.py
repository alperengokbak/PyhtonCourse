try:
    number = int(input("Enter The Number: "))
    print(number)
except (ValueError , ZeroDivisionError):     # We can write two error with "," between brackets like that.
    print("Not connect types variable!!")
except:
    print("Error!")