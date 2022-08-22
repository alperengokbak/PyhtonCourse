import json

data = '{"firstName" : "EA" , "lastName" : "3008"}'     # This data type is called "Json Data"

dataExample = {"firstName" : "Miami" , "Email" : "alperengokbak@gmail.com"}
dataExampleJson = json.dumps(dataExample)
print(dataExample)

x = json.loads(data)

print(x["firstName"])
print(x["lastName"])