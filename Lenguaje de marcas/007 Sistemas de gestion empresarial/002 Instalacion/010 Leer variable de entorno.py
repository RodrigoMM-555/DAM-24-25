# Cone sto podemos guardar varibles en el ordenador que no queremos que este en el codigo

# En el shell (terminal):
# echo 'export NOMBRE="Rodrigo"' >> ~/.bashrc
# source ~/.bashrc
import os

print(os.environ.get("NOMBRE"))