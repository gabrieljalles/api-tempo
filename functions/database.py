import psycopg2
from psycopg2 import OperationalError

database_connected = False

def connect_database(database, user, password, host, port):

    global database_connected
    global connection
    global pg

    if not database_connected:
        connection = psycopg2.connect(
            database= database,
            user= user,
            password= password,
            host= host,
            port= port
        )
        
        pg = connection.cursor()
        print('Database connection established successfully.')
        database_connected = True
        return connection, pg
    else:
        print("Database connection has already been opened")

def disconnect_database():
    
    global database_connected
     
    if database_connected:
        pg.close()
        connection.close()
        database_connected = False
        print('Database connection closed successsfully.')
    else:
        print("Database connection has already been closed or wasn´t opened.")


    

if __name__ == '__main__':
    connect_database("temperatura","postgres","3038","localhost","5432")
    disconnect_database()