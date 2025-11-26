
persona = {
    "nombre":"Rodrigo",
    "apellidos":"Menendez Molina",
    "email":"aja@gmai.com",
    "edad":47,
    "telefonos":[
        {
            "tipo":"fijo",
            "numero":12345678
        },
        {
            "tipo":"movil",
            "numero":87654321
        }
    ]
}

print(persona["telefonos"][1]["numero"])