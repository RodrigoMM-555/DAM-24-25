#sudo apt install python3-pip - Ubuntu
#pip install flask - Windows
#pip3 install flask --breack-system-packages - Linux o macOS

from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    return"funciona"

if __name__ == "__main__":
    aplicacion.run(debug=True)
    
#Puedes ver el link desde la consola
