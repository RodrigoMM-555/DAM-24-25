
#Para usar esto abre una consola cmd para poder correr el ejercicio como en la maquina virtual, con el python3..., pero sin el 3 tipo asi:
#(venv) C:\Users\WorkStation\Documents\GitHub\ProgramacionDAM24-25\Proyecto intemodular\001Falsk\Acts>python "001Python + HTML.py"

from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
  cadena = '''
    <!Doctype html>
    <html>
        <head>
            <title>Flask App</title>
            <style>
                h1{color:red;}
            </style>
        </head>
        <body>
            <h1>Bienvenido a mi aplicación Flask</h1>
            <p>Esta es una página HTML creada con Flask.</p>
  '''
        
  for dia in range(1,31):
    cadena += '<div>'+str(dia)+'</div>' 
         
  cadena += '''
      </body>
    </html>
  '''
  return cadena
  
if __name__ == "__main__":
  aplicacion.run(debug=True)