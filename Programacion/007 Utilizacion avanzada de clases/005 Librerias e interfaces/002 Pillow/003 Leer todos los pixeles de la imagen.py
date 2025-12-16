from PIL import Image

imagen = Image.open("Captura.png")

anchura,altura = imagen.size

for x in range(0,anchura):
    for y in range(0,altura):
        pixel = imagen.getpixel((x, y))
        print(pixel)  


