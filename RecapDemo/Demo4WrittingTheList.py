import os

citys = ["Miami" , "Los Angels" , "Los Santos"]
#%% Creating Text File
""" fileToAppend = open("City.txt" , "a")

for city in citys:
    fileToAppend.write(city)
    fileToAppend.write("\n")
fileToAppend.close """

#%% Removing Text File
if os.path.exists("City.txt"):
    os.remove("City.txt")
else:
    print("The File Already Removed!")
