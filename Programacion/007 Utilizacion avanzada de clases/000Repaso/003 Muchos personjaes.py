
class Npc():
    def __init__(self,x,y):
        self.posx = x
        self.posy = y


personajes = []
numero_personajes = 20

for i in range(0,numero_personajes):
    personajes.append(Npc(4,3))

print(personajes)
print(len(personajes))