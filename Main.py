import psycopg2
import Connect
from Controller import Controller

#Catching errors
try:
    #Making connection
    connection = Connect.makeConnect()
    #Creating cursor to control DB
    cursor = connection.cursor()
    #Controller call
    Controller.mainMenu()

except (Exception , psycopg2.Error) as error :
        print ("PostgreSQL Error: ",error)
finally:
    #Closing connection and cursir
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")
