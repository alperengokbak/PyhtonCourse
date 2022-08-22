#Changing the place of two numbers
x = 10
y = 20

print("x = " , x ,"y = " , y)   #print("x = " + str(x)) Both expression are giving same display.

temp = x    #x,y = y,x that expression special for python. You dont have to use temp to change variables of value
x = y
y = temp

print("x = " , x ,"y = " , y)