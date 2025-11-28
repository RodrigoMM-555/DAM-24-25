
import random

class Npc():
    def __init__(self,x,y):
        self.posx = x
        self.posy = y


personajes = []
numero_personajes = 20

for i in range(0,numero_personajes):
    xAl = random.randint(0,100)
    yAl = random.randint(0,100)
    personajes.append(Npc(xAl,yAl))

print(personajes)
print(len(personajes))