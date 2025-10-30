
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(7,2) NOT NULL,
    stock INT NOT NULL,
    CONSTRAINT chk_nombre_length CHECK (CHAR_LENGTH(nombre) >= 5),
    CONSTRAINT chk_precio CHECK (precio >= 0 AND precio <= 5000),
    CONSTRAINT chk_stock CHECK (stock >= 0)
);

ALTER TABLE productos
  MODIFY id INT NOT NULL,
  ADD PRIMARY KEY (id);

ALTER TABLE productos
  MODIFY id INT NOT NULL AUTO_INCREMENT;

ALTER TABLE productos
  ADD CONSTRAINT chk_stock_no_negativo
  CHECK (stock >= 0);

ALTER TABLE productos
  ADD CONSTRAINT chk_precio_no_negativo
  CHECK (precio >= 0);

ALTER TABLE productos
  ADD CONSTRAINT chk_precio_max_5000
  CHECK (precio <= 5000);

ALTER TABLE productos
  ADD CONSTRAINT chk_nombre_min_5
  CHECK (CHAR_LENGTH(nombre) >= 5);

INSERT INTO productos (nombre, descripcion, precio, stock) VALUES
('Patito Clásico', 'El patito de goma amarillo tradicional.', 3.50, 120),
('Patito Pirata', 'Patito de goma con parche y sombrero pirata.', 4.25, 80),
('Patito Astronauta', 'Patito de goma conc asco de astronauta.', 3.50, 120),
('Patito Ladron', 'Patito de goma con cuchillo.', 4.25, 80),
