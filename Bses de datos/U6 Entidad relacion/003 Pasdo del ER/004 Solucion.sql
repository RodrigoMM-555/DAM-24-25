-- La solución recomendada es unir tablas, pero tambien se puede hacer cun una goreign key
CREATE TABLE Clientes(
	id INT PRIMARY KEY AUTO_INCREMENTAL,
    nombre VARCHAR(255),
    apellidos VARCHAR(255),
    email VARCHAR(255),
    direccion VARCHAR(255),
    DNINIE VARCHAR(15)
);