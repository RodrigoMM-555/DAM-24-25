
class Npc():
    def __init__(self,x,y):
        self.posx = x
        self.posy = y


personajes = []

personajes.append(Npc(4,3))
personajes.append(Npc(5,4))

print(personajes)