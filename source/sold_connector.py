import mysql.connector

# Configure MariaDB connection
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'admin',
    'database': 'STOCK_SOLD'
}


def connect_to_sold_database():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.connector.Error as error:
        return error

def close__connection(connection):
    if connection:
        connection.close()
