import mysql.connector
import time


def connect_to_mysql():
    # Make connection with MySQL
    db = mysql.connector.connect(
        host="mysql",
        user="root",
        password="password",
        database="mydatabase",
        port="3306",
    )

    if db:
        print("Connection stablished correctly.... You done!")


# Esperar 10 segundos antes de intentar la conexión
time.sleep(90)

# Llamar a la función para conectar a MySQL
connect_to_mysql()
