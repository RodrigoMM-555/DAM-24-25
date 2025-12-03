
Crear tabla de productos
Que tenga:

Identificador/Clave primaria
nombre (varchar 255)
descripcion (text)
precio (decimal(5,2))
stock (int)

Restricciones:
stock no puedes ser negativo
precio no pued superar los 5000 euros
el nombre del producto debe tener al menos 5 caracateres


use empresaDAM

create table productos(
    ID int AUTO_INCREMENT PRIMARY KEY FIRST,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    precio decimal(5,2) NOT NULL,
    stock int NOT NULL

CONSTRAINT chk_stock_no_negativo
CHECK (stock >= 0),

CONSTRAINT chk_precio_maximo
CHECK (precio <= 5000),

CONSTRAINT chk_nombre_minimo
CHECK (CHAR_LENGTH(nombre) >= 5)

);

