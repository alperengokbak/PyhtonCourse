def primeMethod():
    number = int(input("Enter The Number: "))
    counter = 0

    for n in range(2 , number):
        if (number % n) == 0:
            counter = counter + 1
            break

    if counter:
        print(number , " Is Not Prime Number.")
    else:
        print(number , " Is Prime Number.")

primeMethod()