from mysql import connector
import os

def solution():
    cnx = connector.connect(
        user="root",
        password=os.environ['DATABASE_PASSWORD'],
        host="127.0.0.1",
        database="sockets_db"
    )

    cursor = cnx.cursor()
    sql = '''DROP DATABASE `sockets_db`'''
    cursor.execute(sql)

    cursor.close()
    cnx.close()


if __name__ == "__main__":
    solution()
