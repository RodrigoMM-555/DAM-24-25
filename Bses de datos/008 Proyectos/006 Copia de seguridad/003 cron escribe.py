
#!/usr/bin/env python3

archivo = open("/ruta/donde/guardar/lineas.txt",'a')
archivo.write("Esta es una linea\n")
archivo.close()

'''
En el cron, añado esta linea:
* * * * * /usr/bin/python3 /var/www/html/003 cron escribe.py 
'''