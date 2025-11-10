
'''
Rodrigo Menendez Molina
Examen trimestre 1 v0.1
Portafolio piezas y categorias
'''

#Librerias a importar
import mysql.connector

#Conexion de suusario para mysql
conexion = mysql.connector.connect(
    host="localhost",
    user="Trimestral1",
    password="Trimestral123$",
    database="portafolioexamen"
)

#Mensaje de entrada
print("-----------------------------")
print("#####Rodrigo Menendez Molina######")
print("###CRUD pieza y categorias v0.1###")

#Bucle y menu
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


##############################################################################################
    #Priemra opcion, añadir pieza
    if opcion == 1:

        cursor = conexion.cursor()

        #Insercion de valores
        print("Insterta la pieza")
        titulo = input("Titulo: ")
        descripcion = input("Descripcion: ")
        fecha = input("Fecha: ")
        id_categoria = input("Identificador categoria: ")

        #Ejecucion de la peticion
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

##############################################################################################

    #Seguna opcion listar piezas
    elif opcion == 2:

        #Cramos el cursor y ejecutamos al consulta, mostramos la vision de piezas y categorias
        cursor = conexion.cursor()
        cursor.execute('''
            SELECT *FROM piezasportafolio;
            ''')

        #Obtenemos las finals
        filas = cursor.fetchall()

        #Mostramos las filas
        if filas:
            for fila in filas:
                print(fila)
        else:
            print("No se encontraron piezas.")

        print("--------------------------------")

        #Mostramos piezas
        cursor.execute('''
            SELECT *FROM vista_piezas;
            ''')

        #Obtenemos las finals
        filas = cursor.fetchall()

        #Mostramos las filas
        if filas:
            for fila in filas:
                print(fila)
        else:
            print("No se encontraron piezas.")
        
        #Peticion terminada
        cursor.close()

##############################################################################################
    #Opcion3, actualizar una pieza
    elif opcion == 3:

        #Pedimos el identificador de la pieza a actualizar
        identificador = input("Identificador de la pieza a actualizar: ")

        #Cambiamos los valores
        titulo = input("Nuevo titulo: ")
        descripcion = input("Nueva descripcion: ")
        fecha = input("Nueva fecha: ")
        id_categoria = input("Nuevo identificador categoria: ")

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
        
        #Peticion terminada
        conexion.commit()

        print("Pieza actualizada")

        #Cerramos la conexion
        cursor.close()

############################################################################################
    #Opcion 4, eliminar una pieza
    elif opcion == 4:

        #Pedimos el identificador de la pieza que se va a a eliminar
        identificador = input("Identificador de la pieza a eliminar: ")

        #Nos conectamos y ejecutamos
        cursor = conexion.cursor()
        cursor.execute('''
        DELETE FROM piezasportafolio WHERE identificador = '''+identificador+'''                       
        ''')

        #Peticion terminada
        conexion.commit()

        print("Pieza borrada")

        #Cerramos la conexion
        cursor.close()

##############################################################################################
    #Opcion 5, salir
    elif opcion == 5:
        break

    #Culaquier otra opcion dara error
    else:
        print("Inavlido")


