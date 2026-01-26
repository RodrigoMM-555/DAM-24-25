# Cone sto podemos guardar varibles en el ordenador que no queremos que este en el codigo

# En el shell (terminal):
# echo 'export CONTRASENA_CEAC="CEAC123$"' >> ~/.bashrc
# source ~/.bashrc
import os

print(os.environ.get("CONTRASENA_CEAC"))