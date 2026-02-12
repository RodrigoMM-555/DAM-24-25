nano index2.html    -> no nos dejara
sudo nano index2.html   -> lo hacemos con sudo
sudo = super user do
sudo nano index3.html


sudo mkdir misuperweb   -> creamos una carpeta
Desde filecilla no nos dejara modificar porque no tenemos permisos

Permisos de linux:
chmod 644   -> propietario puede 6 el resto 4
No sera suficiente

chmod 755   -> menos restrictivo, lo cambiaremos una vez subidos los archivos a 644

sudo chmod 755 -R misuperweb