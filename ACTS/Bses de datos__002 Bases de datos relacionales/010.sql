
-- Crear usuario nuevo con contraseña
CREATE USER 
'UempresaDAM'@'localhost' 
IDENTIFIED  BY 'empresaDAM123$';

-- Dar acceso a ese usuario
GRANT USAGE ON *.* TO 'UempresaDAM'@'localhost';

-- Quitar todos los límites que tenga
ALTER USER 'UempresaDAM'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

-- Darle acceso a la base de datos empresadam
GRANT ALL PRIVILEGES ON `empresaDAM`.* 
TO 'UempresaDAM'@'localhost';

--Recargamos la tabla de privilegios para aplicarlos inmediatamente
FLUSH PRIVILEGES;


