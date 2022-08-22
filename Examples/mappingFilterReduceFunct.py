from functools import reduce

numbers = [1 , 2 , 3 , 4]

multipliedNumbers = list(map(lambda x : x**2 , numbers))    # "lambda" fonksiyonu anlamı şu şekildedir. x'in karesini alır, numbers listesinin içindeki elemanlara uygular.("Numbers" listesinde her bir sayı için, sayının karesini al ve iter ettiğin her değeri listeye ekle.)

filteredNumber = list(filter(lambda x : x > 3 , numbers))   # "Numbers" listesinde "x" eğer verilen sayıdan büyükse bunu listeye ekle analmına gelir. Yanii istenilen değeri filtrelemiş oluyoruz.

factorialNumbers = reduce(lambda x , y : x * y , numbers)   # "Numbers" listesindeki kendi sayıları arasında çarptı. X'in y ile olan ilişkisini kontrol ederken "Reduce" fonksiyonundan yararlanabiliriz.(x * y) değerini x değerine atayıp bir sonraki sayı y olarak devam eder.

print(factorialNumbers)