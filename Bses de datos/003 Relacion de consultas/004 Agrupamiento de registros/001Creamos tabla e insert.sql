--sudo mysql -u root -p

USE clientes

--Creamos la tabla
CREATE TABLE productos(
	nombre VARCHAR(255),
	precio DECIMAL(10,2),
	categoria VARCHAR(255),
	peso DECIMAL(10,2),
	stock INT,
	color VARCHAR(255)
);

--Confirmación de la tabla
SHOW TABLES;
DESCRIBE productos;

--Insert
INSERT INTO productos (nombre, precio, categoria, peso, stock, color) VALUES
('Camiseta básica', 15.99, 'Ropa', 0.2, 50, 'Rojo'),
('Jeans ajustados', 45.00, 'Ropa', 0.6, 30, 'Azul'),
('Zapatos deportivos', 60.00, 'Calzado', 1.2, 25, 'Negro'),
('Mochila de cuero', 70.50, 'Accesorios', 1.0, 15, 'Negro'),
('Chaqueta impermeable', 120.00, 'Ropa', 1.5, 10, 'Verde'),
('Sombrero de paja', 22.00, 'Accesorios', 0.3, 40, 'Beige'),
('Gorra', 15.50, 'Accesorios', 0.2, 50, 'Rojo'),
('Bermuda de baño', 18.00, 'Ropa', 0.3, 45, 'Azul'),
('Cinturón de cuero', 30.00, 'Accesorios', 0.5, 20, 'Marrón'),
('Camisa de lino', 40.00, 'Ropa', 0.4, 35, 'Blanco'),
('Pantalón de vestir', 55.00, 'Ropa', 0.8, 20, 'Negro'),
('Socks deportivos', 10.00, 'Ropa', 0.1, 100, 'Blanco'),
('Bolsos de mano', 90.00, 'Accesorios', 0.8, 12, 'Negro'),
('Botines de cuero', 85.00, 'Calzado', 1.3, 22, 'Negro'),
('Sandalias playeras', 25.00, 'Calzado', 0.5, 40, 'Beige'),
('Camiseta estampada', 18.00, 'Ropa', 0.2, 60, 'Rojo'),
('Blusa de seda', 70.00, 'Ropa', 0.3, 15, 'Blanco'),
('Sudadera con capucha', 55.00, 'Ropa', 0.7, 30, 'Gris'),
('Pantalón de mezclilla', 50.00, 'Ropa', 0.8, 60, 'Azul'),
('Zapatillas de running', 65.00, 'Calzado', 1.1, 25, 'Azul'),
('Cinturón deportivo', 20.00, 'Accesorios', 0.3, 50, 'Negro'),
('Chaqueta de lana', 110.00, 'Ropa', 1.2, 8, 'Rojo'),
('Gafas de sol', 30.00, 'Accesorios', 0.1, 70, 'Negro'),
('Botas de montaña', 120.00, 'Calzado', 1.5, 18, 'Negro'),
('Faldas de mezclilla', 35.00, 'Ropa', 0.5, 40, 'Azul'),
('Polo de algodón', 25.00, 'Ropa', 0.2, 50, 'Verde'),
('Chaleco de abrigo', 75.00, 'Ropa', 0.6, 15, 'Gris'),
('Pantalón de jogging', 30.00, 'Ropa', 0.6, 50, 'Negro'),
('Camisón de seda', 45.00, 'Ropa', 0.2, 12, 'Blanco'),
('Zapatillas deportivas', 55.00, 'Calzado', 1.0, 35, 'Negro'),
('Cartera de cuero', 50.00, 'Accesorios', 0.4, 28, 'Marrón');


