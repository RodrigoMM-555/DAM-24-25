import random
import json
from flask import Flask,render_template

#Definimos la clase
class Npc():
    def __init__(self, x, y,radio):
        self.posx = x
        self.posy = y
        self.radio = radio

    # Método para convertir el objeto en diccionario
    def to_dict(self):
        return {"posx": self.posx, "posy": self.posy}

# Preparo los personajes las listas y cantidades
personajes = []
numero_personajes = 50

#Creamos los personajes
for i in range(0, numero_personajes):
    xAleatoria = random.randint(0, 500)
    yAleatoria = random.randint(0, 500)

    personajes.append(Npc(xAleatoria, yAleatoria))

#Lo convertino en estructura json
personajes_json = [p.to_dict() for p in personajes]

# Lanzo una web
app = Flask(__name__)

#App para el juego
@app.route("/")
def inicio():
  return render_template("juego.html")

#App para el json
@app.route("/api")
def api():
  return json.dumps(personajes_json, indent=2)
  
if __name__ == "__main__":
  app.run(debug=True)