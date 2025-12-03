
insert into clientes values(
    NULL,
    "12345678A",
    "Poronga",
    "Merenge",
    "jaja@gmail.com"
);
ERROR 3819 (HY000): Check constraint 'comprobar_dni_nie_letra' is violated.


insert into clientes values(
    NULL,
    "12345678A",
    "Poronga",
    "Merenge",
    "jajaom"
);
ERROR 3819 (HY000): Check constraint 'comprobar_dni_nie_letra' is violated.

INSERT INTO clientes VALUES(
	NULL,
	"12345678Z",
	"Rodrigo",
	"Menendez",
	"aja@gmail.com",
	"maestro"
);
#Este funcionara