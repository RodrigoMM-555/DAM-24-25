CREATE TABLE cliente (
  id INT PRIMARY KEY,
  nombre VARCHAR(255),
  apellidos VARCHAR(255),
  email VARCHAR(255)
);

CREATE TABLE pedido (
  id INT PRIMARY KEY,
  fecha VARCHAR(255),
  cliente_id INT,
  CONSTRAINT fk_pedido_1 FOREIGN KEY (cliente_id) REFERENCES cliente(id)
);

CREATE TABLE producto (
  id INT PRIMARY KEY,
  nombre VARCHAR(255),
  precio VARCHAR(255)
);

CREATE TABLE lineapedido (
  id INT PRIMARY KEY,
  prodructo_id INT,
  pedido_id INT,
  CONSTRAINT fk_lineapedido_1 FOREIGN KEY (prodructo_id) REFERENCES producto(id),
  CONSTRAINT fk_lineapedido_2 FOREIGN KEY (pedido_id) REFERENCES pedido(id)
);