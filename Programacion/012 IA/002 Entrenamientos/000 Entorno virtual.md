Primero tenemos que crear un entorno virtual
Es una burbuja aislada que no afecta al resto del sistema
En la terminal:

instala venv
sudo apt install python3.12-venv

usa venv
python3 -m venv venv

A continuación, entramos dentro del entorno
En la terminal:

source venv/bin/activate

Esto de momento no
//pip install -r 001.2 Librerias requeridas.txt

Requerimientos
pip install torch
pip install datasets
pip install peft
pip install transformers

Estamos creando un entorno virtual con venv y entrandop para instalar las librerias que necesitamos, de esta forma si hay que mover todo con llevarnos el venv que es el entorno cirtual tambien te llevas las librerias.