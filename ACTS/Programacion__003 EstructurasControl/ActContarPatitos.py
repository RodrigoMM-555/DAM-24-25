
'''
Rodrigo Menendez Molina
003/002 Estructuras de repeticion
Contador de patitos
'''

total=0

for año in range(1978,2026):
    for mes in range(1,13):
        for dia in range(1,31):
            total+=10
            print("Dia",dia,"del mes",mes,"del año",año,"se han fabricado 10 patitos de goma")
            print("En total se han fabricado",total,"patitos de goma")
