
from flask import Flask, render_template_string
import json

app = Flask(__name__)

@app.route("/")
def cv():
    with open("curriculum.json",encoding="utf-8") as f:         #Ahora f es el codigo del archivo .json
        data = json.load(f)                                     #data es igual al contenido que se carga de f, que es .json
    dp = data["datos personales"]                               #dp es el apartado datos personales de f, que el archivo .json

    with open("curriculum.html", encoding="utf-8") as f:       #Ahora f es el archivo html
        html = f.read()                                         #y ahora la variable html es el contenido leido del archivo html que ahora se llama f

    return render_template_string(html,**dp)

if __name__ == "__main__":
    app.run(debug=True)