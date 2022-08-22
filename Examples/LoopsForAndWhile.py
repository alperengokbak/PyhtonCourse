city = ["Miami" , "Berlin" , "Copenhagen" , "Stockholm"]

# For Loops
for city in city:
    if len(city) > 3:
        print(city)
        print(city[1 : 3])  # Display second letter to third letter. You can change the request instead of "1" or "3".

# While Loops
counter = 1
result = 0

while counter <= 10:
    result += counter
    counter = counter + 1
print(result)