CREATE USER 
'[tunombredeusuario]'@'[tuservidor]' 
IDENTIFIED  BY '[tucontraseña]';

GRANT USAGE ON *.* TO '[tunombredeusuario]'@'[tuservidor]';

ALTER USER '[tunombredeusuario]'@'[tuservidor]' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;


GRANT ALL PRIVILEGES ON [tubasededatos].* 
TO '[tunombredeusuario]'@'[tuservidor]';

FLUSH PRIVILEGES;

