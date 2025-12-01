--Dos tabals con una forign key
CREATE TABLE cliente (
  id INT PRIMARY KEY,
  nombre VARCHAR(255),
  apellidos VARCHAR(255)
);

CREATE TABLE entidad (
  id INT PRIMARY KEY,
  id_cliente VARCHAR(255),
  tipo VARCHAR(255),
  numero VARCHAR(255),
  CONSTRAINT fk_entidad_1 FOREIGN KEY (id_cliente) REFERENCES cliente(id)
);