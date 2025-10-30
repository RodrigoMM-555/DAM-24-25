
'''
Rodrigo Menendez Molina
Examen U2 v0.1
Planificador de cuadras
'''
import math
import datetime as datet

#Inicializacion
print("------------------------------------")
print("##### Planificador de cuadras  #####")
print("##### Rodrigo Menendez Molina  #####")

#Datos de entrada
caballos = int(input("Caballos: "))
capacidad_por_cuadra = int(input("Capacidad por cuadra: "))
fecha = input("Fecha(YYYY-MM-DD): ")

#Calculo de cuadras
cuadras_necesarias = math.ceil(caballos / capacidad_por_cuadra)

#Fechas
year,month,day = fecha.split("-")
hoy = datet.date(int(year),int(month),int(day))
#Se que estoy empleando pasos de más pero es para demostrar dominio sobre los metodos de la libreria

diadelasemana = hoy.isoweekday()
if diadelasemana < 6:
    cuando_cae = " entre semana."
elif diadelasemana >= 6:
    cuando_cae = " fin de semana."

print("-------------------------------------------------------")
print("Hoy es",hoy.day,"del",hoy.month,"de",hoy.year,"y es"+cuando_cae)
print("Hay",caballos,"caballos")
print("Caben",capacidad_por_cuadra,"caballos por cuadra")
print("Se necesitaran",cuadras_necesarias,"cuadras")
print("-------------------------------------------------------")

