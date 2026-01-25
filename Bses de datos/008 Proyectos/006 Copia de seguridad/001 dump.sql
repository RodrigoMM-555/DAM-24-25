sudo mysql -u root -p

SHOW DATABASES;

Una vez conocemos el nombre de la base de datos
Me voy a la terminal y escribo:

sudo mysql -u root -p nombre_base_de_datos > /ruta/al/archivo/BD_dump.sql

Y paara traerlo seria:

sudo mysql -u root -p nombre_base_de_datos < /ruta/al/archivo/BD_dump.sql


Esto con un script automatizado cada cierto tiempo nos permite tener copias de seguridad de nuestras bases de datos, periodicamente.
Para eso podemos unasr crontab, en ubuntu.
