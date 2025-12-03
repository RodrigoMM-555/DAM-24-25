
ALTER TABLE clientes
ADD COLUMN identificador INT AUTO_INCREMENT PRIMARY KEY FIRST;


ALTER = Altera
TABLE = Tabla
clientes = nombre de la tabla
COLUMN = quiero añadir una columna
identificador = nombre de la columna a añadir
INT = tipo de valor (debe ser entero en este caso), como no es null si o si debe tenre algo
PRIMARY KEY = Clave primaria
FIRST = Esta debe ser la primera en caso de haber varias columnasç


DESCRIBE clientes;	#Para ver si lo hemos ehcho bien

#Por mucho que se repitan los datos el identificador
es distinto y nunca se repetira, incluso si borramos
el anterior. Pese a que tenga null el programa se 
encarga de poner el numero.

INSERT INTO clientes VALUES(
	NULL,
	"12345678A",
	"Rodrigo",
	"Menendez",
	"aja@gmail.com",
	"maestro"
);	