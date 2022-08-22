import sys

list = [6 , 'Alperen' , 3 , 0 , "26"]

for i in list:
    try:    
        print("Number: " + str(i))
        result = 1 / int(i)
        print("Result: " + str(result))
        print("*****")
    except ValueError:
        print(str(i) + " is not number!")
    except ZeroDivisionError:
        print(str(i) + " cant divide by zero!")
    except:
        print(str(i) + " Not Calculated!")
        print("The System Gave Error: " + str(sys.exc_info()[0]))   # This command give to us type of error with type of array.
    finally:    # Finally command works every scenario. It can be showing changes, after "try" or "except" commands.
        print("Processes still working...")
