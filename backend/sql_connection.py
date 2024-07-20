import mysql.connector
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

__cnx = None

def get_sql_connection() :
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(
          host=os.getenv("DATABASE_HOST"),
          user=os.getenv("DATABASE_USER"),
          password=os.getenv("SQL_PASSWORD"),
          database=os.getenv("DATABASE_NAME")
        )
    return __cnx