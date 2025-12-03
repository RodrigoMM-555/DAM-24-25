
sudo mysql -u root -p

use empesaDAM;

show tables;

describe clientes;

select * from clientes;

insert into clientes values(
    NULL,
	"12345678A",
	"Rodrigo",
	"Menendez",
	"aja@gmail.com"
);

    #REGEXP son las esxpresiones regulaes, no hay que 
    aprendersaelas, se puden buscar en cahtgpt o internet
    #Esto es para evitar que se metan datos que
    que no se deben meter en email

ALTER TABLE clientes
  ADD CONSTRAINT comprobar_email
  CHECK (email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$');

    #Si ya hay datos metidos con valores invalidos habra
    que eliminarlos
delete from clientes where identificador = 7;

    #Por ejemplo este seria invalido 
insert into clientes values(
    NULL,
	"12345678A",
	"Rodrigo",
	"Menendez",
	"algo"
);
ERROR 3819 (HY000): Check constraint 'comprobar_email' is violated.
    #Ahora que hemos puesto al restriccion no nos
    dejara meter datos invalidos


