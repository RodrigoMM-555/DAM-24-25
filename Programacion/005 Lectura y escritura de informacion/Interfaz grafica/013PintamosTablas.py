
import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

#Treeviw crea una tabla
arbol = ttk.Treeview(ventana,columns=("nombre","apellidos"), show="headings")
arbol.heading("nombre",text="Nombre del cliente: ")
arbol.heading("apellidos",text="Apellidos del cliente: ")

arbol.insert("","end",values=("Rodrigo","Menendez Molina"))
arbol.insert("","end",values=("Mario","Bas Cortes"))

arbol.pack(padx=20,pady=20)

ventana.mainloop()
