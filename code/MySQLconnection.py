import mysql.connector


def connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',  
        password='admin',  
        database='ParkFindr'
    )
    return connection

