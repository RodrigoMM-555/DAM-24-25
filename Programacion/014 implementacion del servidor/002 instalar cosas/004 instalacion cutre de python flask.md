En el servidor ya tenemos python3
Pero no tenemos pip

sudo apt install python3-pip
pip3 install flask --break-system-packages

Para solo un proyecto crearemos un entorno virtual
es decir instalar los pluggins en la carpeta del prioyecto

Por otro lado si el plugin e spara varios lo instalaremos en la
raiz usando el break system packages

cd /home/jocarsa

mkdir proyectoflask1

cd proyectoflask1

Para poder usar flask tendremos que añadir a la ip :5000
esto porque apache ya esta gastando el puerto 80 por lo que
si desactivamos apache podremos usarlo

Parar apache:
sudo service apache2 stop