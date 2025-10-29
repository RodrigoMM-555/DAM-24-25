
'''
Rodrigo Menéndez Molina
004 / 006 utilización de clases y objetos 
Creación de clase matemáticas
'''

class Matematicas():
    def __init__(self):
        self.Pi = 3.141592
        
    def redondeo(self,numero):      #Redondeo normal
        entero = int(numero)
        decimal = numero - entero
        if decimal < 0.5:
            redondeo = 0
        else:
            redondeo = 1
        return entero + redondeo
        
    def techo(self,numero):         #Redondeo a la alta
        return int(numero) + 1
    def suelo(self,numero):         #Redondeo a la baja
        return(int(numero))
        

mate = Matematicas()

print(mate.redondeo(4.7))
print(mate.redondeo(4.2))

print(mate.techo(4.7))
print(mate.suelo(4.7))
