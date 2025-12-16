from PIL import Image

imagen = Image.open("Captura.png")

tamanio = imagen.size
print(tamanio)

print("anchura:",tamanio[0])
print("altura:",tamanio[1])

pixel1 = imagen.getpixel((0, 0))

print(pixel1)
