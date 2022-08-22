from select import select


def addition(number1 , number2):
    return number1 + number2

def substraction(number1 , number2):
    return number1 - number2

def multiplication(number1 , number2):
    return number1 * number2

def division(number1 , number2):
    return number1 / number2

def menu():
    print(
    "Select Your Option:" + "\n"
    + "0-) Exit From Calculator." + "\n"
    + "1-) Addition." + "\n"
    + "2-) Subtraction." + "\n"
    + "3-) Multiplication." + "\n"
    + "4-) Division." + "\n"
    + "5-) Back To Menu.")