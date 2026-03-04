
import pickle

class Cliente():
    def __init__(self):
        self.nombre = ""
        self.email = ""

cliente1 = Cliente()

cliente1.nombre = "Jose Vicente"
cliente1.email = "aja@gmail.com"

archivo = open("clientes.bin","wb")
pickle.dump(cliente1,archivo)
archivo.close()

archivo = open("clientes.bin","rb")
cliente1 = pickle.load(archivo)
print(cliente1.nombre,cliente1.email)