from genericpath import exists
import os
#%% Open File
file = open("customer.txt" , "r")  # Provide to read that file.("r" read)
#%% Write On The File
file = open("customer.txt" , "w")   # That command("w" write) provide create a "txt file". During writting can be remove the whole data. Because writes new data on the other data.
#%% Append Variable To File
file = open("customer.txt" , "a") # That command ("a" append) similiar to ("w") but there is a different from "w". It will create and write inside at the same time.
#%% Create A File
file = open("customer.txt" , "x")  # That command("x" create) create a file but if there is same named that file, give error for us.
#%% Reading Commands
print(file.readlines())   # Gives to us that output:['Miami\n', 'Los Angels\n', 'California\n', 'Washington']
print(file.read())   # It just read first "5" char.
print(file.readline())   # Allows to read line by line

file.close 
#%% Remove Command
if os.path.exists("customer.txt"):      # That command control is there any file named "customer.txt". If there is, will remove.
    os.remove("customer.txt")
else:
    print("The File Already Removed!")

os.rmdir("empty")   # That command remove the file named of what is the between brackets.