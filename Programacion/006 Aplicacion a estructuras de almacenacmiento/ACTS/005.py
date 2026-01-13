import re

#Variable que contiene la dirección
direccion = "Calle Mayor 12 B 28013"

#Patrón de validación: calle con letras (permitiendo acentos y espacios), número de portal, letra opcional separada por espacio, y código postal de 5 dígitos
patron = r"^[A-Za-záéíóúÁÉÍÓÚ\s]+ \d+\s?[A-Za-z]? \d{5}$"

#Validar la dirección
if re.match(patron, direccion):
    print("Dirección correcta")
else:
    print("Dirección incorrecta")