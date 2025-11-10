'''
Rodrigo Menendez Molina
Examen trimestre 1 v0.1
Portafolio piezas y categorías
'''

#Librerias a importar
import mysql.connector

#Conexión del usuario para mysql
conexion = mysql.connector.connect(
    host="localhost",
    user="Trimestral1",
    password="Trimestral123$",
    database="portafolioexamen"
)

#Mensaje de entrada
print("-----------------------------")
print("#####Rodrigo Menendez Molina######")
print("###CRUD pieza y categorías v0.1###")

#Bucle y menú
while True:
    print("-----------------------------")
    print("-------Menu-------")
    print("1. Añadir pieza")
    print("2. Listar piezas")
    print("3. Actualizar pieza")
    print("4. Eliminar pieza")
    print("5. Salir")
    opcion = int(input("Que pocion quieres: "))
    print("-----------------------------")


###################################################################################

    #Primera opción, añadir pieza
    if opcion == 1:

        cursor = conexion.cursor()

        #Inserción de valores
        print("Inserta la pieza")
        titulo = input("Título: ")
        descripcion = input("Descripción: ")
        fecha = input("Fecha: ")
        id_categoria = input("Identificador categoría: ")

        #Ejecución de la petición
        cursor.execute('''
            INSERT INTO piezasportafolio
            VALUES(
                NULL,
                "'''+titulo+'''",
                "'''+descripcion+'''",
                "'''+fecha+'''",
                '''+id_categoria+'''
                );
            ''')

        #Peticion teminada
        conexion.commit()

        print("Pieza añadida correctamente")

        cursor.close()

###################################################################################

    #Segunda opción listar piezas
    elif opcion == 2:

        #Creamos el cursor 
        cursor = conexion.cursor()
				
		#Mostramos las piezas
        cursor.execute('''
            SELECT *FROM piezasportafolio;
            ''')

        #Obtenemos las filas
        filas = cursor.fetchall()

        #Mostramos las filas
        if filas:
            for fila in filas:
                print(fila)
        else:
            print("No se encontraron piezas.")

        print("--------------------------------")

        #Mostramos la peticion cruzada
        cursor.execute('''
            SELECT *FROM vista_piezas;
            ''')

        #Obtenemos las filas
        filas = cursor.fetchall()

        #Mostramos las filas
        if filas:
            for fila in filas:
                print(fila)
        else:
            print("No se encontraron piezas.")
        
        #Petición terminada
        cursor.close()

###################################################################################

    #Opción 3, actualizar una pieza
    elif opcion == 3:

        #Pedimos el identificador de la pieza a actualizar
        identificador = input("Identificador de la pieza a actualizar: ")

        #Cambiamos los valores
        titulo = input("Nuevo título: ")
        descripcion = input("Nueva descripción: ")
        fecha = input("Nueva fecha: ")
        id_categoria = input("Nuevo identificador categoría: ")

        #Nos conectamos y ejecutamos
        cursor = conexion.cursor()
        cursor.execute('''
            UPDATE piezasportafolio
            SET titulo = "'''+titulo+'''",
                descripcion = "'''+descripcion+'''",
                fecha = "'''+fecha+'''",
                id_categoria = "'''+id_categoria+'''"
                WHERE identificador = "'''+identificador+'''";
            ''')
        
        #Petición terminada
        conexion.commit()

        print("Pieza actualizada")

        #Cerramos la conexión
        cursor.close()

###################################################################################

    #Opción 4, eliminar una pieza
    elif opcion == 4:

        #Pedimos el identificador de la pieza que se va a a eliminar
        identificador = input("Identificador de la pieza a eliminar: ")

        #Nos conectamos y ejecutamos
        cursor = conexion.cursor()
        cursor.execute('''
        DELETE FROM piezasportafolio WHERE identificador = '''+identificador+'''                       
        ''')

        #Petición terminada
        conexion.commit()

        print("Pieza borrada")

        #Cerramos la conexión
        cursor.close()

###################################################################################

    #Opción 5, salir
    elif opcion == 5:
        break

    #Cualquier otra opción dará error
    else:
        print("Inavlido")
