import mysql.connector
from mysql.connector import errorcode
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(dotenv_path='../dev.env')


def get_db_connection():
    # database_config = {
    #     'user': os.getenv('user'),
    #     'password': os.getenv('DB_PASSWORD'),
    #     'host': os.getenv('DB_HOST'),
    #     'database': os.getenv('DB_NAME'),
    #     'raise_on_warnings': bool(os.getenv('RAISE_ON_WARNING'))
    # }

    database_config = {
        'user': 'root',
        'password': '12345678',
        'host': 'localhost',
        'database': 'coaching',
        'raise_on_warnings': True
    }

    print(database_config)

    try:
        db_connection = mysql.connector.connect(**database_config)
        print(db_connection)
        return db_connection
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)