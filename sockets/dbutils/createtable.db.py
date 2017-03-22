from mysql import connector
from mysql.connector.errors import ProgrammingError
import os


def solution():
    cnx = connector.connect(
        user="root",
        password=os.environ['DATABASE_PASSWORD'],
        host="127.0.0.1",
        database="sockets_db"
    )

    cursor = cnx.cursor()

    sql1 = """CREATE TABLE Raw
        (
            id int auto_increment,
            ip varchar(15),
            cpu float(5,2),
            ram int,
            timestamp datetime(6),
            PRIMARY KEY(id)
        )"""
    try:
        cursor.execute(sql1)
    except ProgrammingError as e:
        print e

    cursor.close()
    cnx.close()


if __name__ == "__main__":
    solution()
