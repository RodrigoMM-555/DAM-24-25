#si el archivo se llama igula que la libreria dara un error circular

import tkinter as tk    #Esto es un name space, mete toda la libreira en la palabra

def accion():
    etiqueta.config(text="LO HAS PULSADO")

ventana = tk.Tk()

tk.Button(ventana,text="Pulsame si te atreves",command=accion).pack(padx=10,pady=10)

etiqueta = tk.Label(text="¿Has pulsado el boton?")
etiqueta.pack(padx=10,pady=10)      #El pack es par dar los amrgenes, por ahora

ventana.mainloop()      #Es decir, no te salgas de la ventana

