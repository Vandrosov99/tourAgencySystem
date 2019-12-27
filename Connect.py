import psycopg2

#Function that returns connection to DB
def makeConnect():
    return psycopg2.connect(
        user="postgres",
        password="021999",
        host="127.0.0.1",
        port="5432",
        database="tourAgency",
    )
#Function that closes connection to DB
def closeConnect(connection):
    connection.commit()
    connection.close()
