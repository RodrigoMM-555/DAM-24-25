
describe clientes;

#Añadira la columna direeccion
alter table clientes
add column direccion VARCHAR(255);

describe clientes;

#Quitara al columna direccion
alter table clientes
drop column direccion;

describe clientes;

#Cambaira el nombre de la columna dni
aunque no deja porque hay una nomra para esa columna
alter table clientes
rename column dni to dninie;

