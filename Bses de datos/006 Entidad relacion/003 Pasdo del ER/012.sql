CREATE TABLE Clientes(
    id INT PRIMARY KEY AUTO_INCREMENTAL,
    nombre VARCHAR(255),
    apellidos VARCHAR(255),
    email VARCHAR(255)
);


CREATE TABLE Pedido(
    id INT PRIMARY KEY AUTO_INCREMENTAL,
    cliente_id INT,
    fecha VARCHAR(255)
);

CREATE TABLE Producto(
    id INT PRIMARY KEY AUTO_INCREMENTAL,
    nombre VARCHAR(255)
);

CREATE TABLE LineaPedido(
    id INT PRIMARY KEY AUTO_INCREMENTAL,
    pedido_id VARCHAR(255),
    producto_id VARCHAR(255),
    cantidad INT
);