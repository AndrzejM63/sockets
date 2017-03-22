from mysql import connector
from mysql.connector.errors import ProgrammingError
import os


def solution():
    cnx = connector.connect(
        user="root",
        password=os.environ['DATABASE_PASSWORD'],
        host="127.0.0.1",
    )

    cursor = cnx.cursor()
    try:
        cursor.execute("CREATE DATABASE sockets_db")
    except ProgrammingError:
        pass

    cursor.close()
    cnx.close()


if __name__ == "__main__":
    solution()
