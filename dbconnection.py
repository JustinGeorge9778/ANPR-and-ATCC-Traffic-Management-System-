# dbconnection.py
import pymysql

def get_connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='12345678',
        database='mydb',
        port=3306
    )
    return conn