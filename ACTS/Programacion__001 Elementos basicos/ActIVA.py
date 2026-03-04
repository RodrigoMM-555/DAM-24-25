
'''
Rodrigo Menéndez Molina
001/006 Operadores y extensiones
Calculadora de impuestos
'''

#1
base_imponible=0
tatal_iva=0
total_factura=0

#2
base_imponible=float(input("Dame la base imponible: "))

#3
total_iva=base_imponible*(0.21)
total_factura=base_imponible+total_iva

#4
print("El total del IVA es",total_iva,"y el total de la factura es",total_factura)




