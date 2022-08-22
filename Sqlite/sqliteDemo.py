from multiprocessing import connection
import sqlite3

connection = sqlite3.connect("Sqlite/chinook.db")
 #%% Example Select
def selectOperation():
    cursor = connection.execute("""select FirstName , LastName from customers 
                                Where City = 'Prague' or City = 'Berlin'
                                order by FirstName""")   # We orders ascending if we want to order from last data, "(desc)ending" keywords useful for us.
    for row in cursor:
        print("First Name: " + row[0])
        print("Last Name: " + row[1])
        print("******")
    connection.close()
# selectOperation()
#%% Example group by , having , order by
def groupByHavingOrder():
    cursor = connection.execute("""select city , count(*) from Customers group by City having count(*) > 1 order by City""")

    for row in cursor:
        print("City: " + row[0])
        print("Count: " + str(row[1]))
        print("******")
    connection.close()
# groupByHavingOrder()
#%% Example Like
def likeFunction():
    cursor = connection.execute("""select FirstName , LastName from customers 
                                Where FirstName like '%ja'""")
    for row in cursor:
        print("First Name: " + row[0])
        print("Last Name: " + row[1])
        print("******")
    connection.close()
# likeFunction()
#%% Insert Command
def instertCustomer():
    connection.execute("""insert into customers (firstName , lastName , city , email) values('Alperen' , 'Gokbak' , 'Miami' , 'alperengokbak@gmail.com')""")
    connection.commit()
    connection.close()
# instertCustomer()
#%% Update Command
def updateCustomer():
    connection.execute("""update customers set city = 'NewYork' where city = 'Miami' and FirstName = 'Alperen'""")

    connection.commit()
    connection.close()
# updateCustomer()
#%% Delete Operation
def deleteCustomer():
    connection.execute("""Delete from customers
                        where customerid = 60""")
    connection.commit()
    connection.close()
# deleteCustomer()
#%% Join Operation
def joinOperation():
    cursor = connection.execute("""select albums.Title , artists.Name from artists
                                    inner join albums
                                    on artists.ArtistId = albums.AlbumId""")
    for row in cursor:
        print("Title: " + row[0] + "First Name: " + row[1])

    connection.close()
joinOperation()