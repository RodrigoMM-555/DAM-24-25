
import sqlite3

conexion = sqlite3.connect("empresa.db")

cursor = conexion.cursor()

nombre = input("Nombre: ")
apellidos = input("Apellidos: ")
email = input("Email: ")


cursor.execute("""
    INSERT INTO clientes VALUES(
        NULL, '"""+nombre+"""','"""+apellidos+"""','"""+email+"""'
    );
""")

conexion.commit()