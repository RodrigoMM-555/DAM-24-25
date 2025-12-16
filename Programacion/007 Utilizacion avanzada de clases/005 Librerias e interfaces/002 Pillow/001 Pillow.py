#Los png tienen 4 numeros, el ultimo es transparencia, los jpg tiene solo tres que son el red green and blue
from PIL import Image

imagen = Image.open("Captura.png")

pixel1 = imagen.getpixel((0, 0))

print(pixel1)
