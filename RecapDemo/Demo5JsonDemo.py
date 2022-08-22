import json

myPath = 'C:/Users/HP/vsCode/python/RecapDemo/users.json'
with open(myPath) as users:   # We can read the file "with open" command type.
    data = json.load(users)

    for user in range(5):
        print(data[user]["username"])
        print(data[user]["email"])
        print(data[user]["address"]["street"])
        print("*****")
