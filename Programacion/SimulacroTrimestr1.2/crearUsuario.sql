
-- Esto era para crear un usuario con permisos 
-- para el ejercioc 009

--Ahora lo usamos para el simulacro2 del examen1

-- Crea usuario nuevo con contraseña
CREATE USER 
'Usimulacro'@'localhost' 
IDENTIFIED  BY 'Simulacro123$';

-- permite acceso a ese usuario
GRANT USAGE ON *.* TO 'Usimulacro'@'localhost';

-- quitale todos los limites que tenga
ALTER USER 'Usimulacro'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

-- dale acceso a la base de datos empresadam
GRANT ALL PRIVILEGES ON `simulacro`.* 
TO 'Usimulacro'@'localhost';

-- recarga la tabla de privilegios
FLUSH PRIVILEGES;