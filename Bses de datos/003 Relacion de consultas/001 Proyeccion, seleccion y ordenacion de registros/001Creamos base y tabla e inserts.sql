-- sudo mysql -u root -p

CREATE DATABASE clientes;

USE clientes;

--Creamos la tabla
CREATE TABLE clientes(
	nombre VARCHAR(255),
	apellidos VARCHAR(255),
	edad INT
);

--Inserts, 30 clientes
INSERT INTO clientes VALUES("Juan","Lopez",45);
INSERT INTO clientes VALUES("Juan", "Lopez", 45);
INSERT INTO clientes VALUES("Ana", "Gomez", 34);
INSERT INTO clientes VALUES("Carlos", "Martinez", 28);
INSERT INTO clientes VALUES("Maria", "Hernandez", 52);
INSERT INTO clientes VALUES("Pedro", "Perez", 61);
INSERT INTO clientes VALUES("Laura", "Rodriguez", 39);
INSERT INTO clientes VALUES("Miguel", "Sanchez", 44);
INSERT INTO clientes VALUES("Sandra", "Fernandez", 30);
INSERT INTO clientes VALUES("Luis", "Gonzalez", 48);
INSERT INTO clientes VALUES("Carmen", "Diaz", 36);
INSERT INTO clientes VALUES("Raul", "Lopez", 50);
INSERT INTO clientes VALUES("Elena", "Garcia", 41);
INSERT INTO clientes VALUES("Ricardo", "Martinez", 55);
INSERT INTO clientes VALUES("Patricia", "Perez", 27);
INSERT INTO clientes VALUES("David", "Rodriguez", 60);
INSERT INTO clientes VALUES("Isabel", "Sanchez", 38);
INSERT INTO clientes VALUES("Fernando", "Hernandez", 47);
INSERT INTO clientes VALUES("Beatriz", "Lopez", 33);
INSERT INTO clientes VALUES("Javier", "Fernandez", 62);
INSERT INTO clientes VALUES("Esther", "Gonzalez", 29);
INSERT INTO clientes VALUES("Sofia", "Moreno", 41);
INSERT INTO clientes VALUES("Antonio", "Ruiz", 54);
INSERT INTO clientes VALUES("Cristina", "Vazquez", 32);
INSERT INTO clientes VALUES("Alberto", "Torres", 45);
INSERT INTO clientes VALUES("Natalia", "Jimenez", 38);
INSERT INTO clientes VALUES("Oscar", "Martín", 50);
INSERT INTO clientes VALUES("Victoria", "Castro", 43);
INSERT INTO clientes VALUES("Manuel", "Fernandez", 59);
INSERT INTO clientes VALUES("Susana", "Rodriguez", 49);

--
