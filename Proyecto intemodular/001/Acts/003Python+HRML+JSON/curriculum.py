
from flask import Flask, render_template_string
import json

app = Flask(__name__)

@app.route("/")
def cv():
    #Combertimos a f en el archivo json
    with open("curriculum.json",encoding="utf-8") as f:
        #Data es igual al contenido que se carga de f, que es el archivo json
        data = json.load(f)

    #dp es el apartado datos personales de data, que la informacion del archivo json
    dp = data["datos personales"]

    #Ahora f es el archivo html
    with open("curriculum.html", encoding="utf-8") as f:
        #Y ahora la variable html es el contenido leido de f, que es el archivo HTML
        html = f.read()

    #Devolvemos el contenido del archivo HTML con la informacion sustituida del json
    return render_template_string(html,**dp)

if __name__ == "__main__":
    app.run(debug=True)                 