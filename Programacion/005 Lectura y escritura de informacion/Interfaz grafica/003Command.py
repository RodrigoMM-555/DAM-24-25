#si el archivo se llama igula que la libreria dara un error circular

import tkinter as tk    #Esto es un name space, mete toda la libreira en la palabra

def accion():
    print("LO HAS PULSADO")

ventana = tk.Tk()

tk.Button(ventana,text="Pulsame si te atreves",command=accion).pack(padx=10,pady=10)

ventana.mainloop()      #Es decir, no te salgas de la ventana

