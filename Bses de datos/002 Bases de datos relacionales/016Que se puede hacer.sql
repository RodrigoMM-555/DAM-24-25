016Que se puede hacer NULL

#Puetsa en escena
sudo mysql -u root -p;
show tables;
use empresaDAM;
show table;

#Nueva tabla
CREATE TABLE pedidos(
	numeropedido VARCHAR (20) NOT NULL,
	cliente VARCHAR (50) NOT NULL,
	producto VARCHAR(255) NOT NULL
);
	
	
	
