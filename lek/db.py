from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="10.130.0.219",
        user=input("Имя пользователя: "),
        password=getpass("Пароль: "),
    ) as connection:
        print(connection)
except Error as e:
    print(e)