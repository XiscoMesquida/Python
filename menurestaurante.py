import sqlite3
from tkinter import *

#Configuración de la raíz

root = Tk()
root.title("Can Xisco - Carta")
root.resizable(0,0)
root.config(bd = 25, relief = "sunken")

Label(root, text = "   Can Xisco  ", fg = "lightblue", font = ("Time New Roman", 28, "bold italic")).pack()
Label(root, text = "-Cuina Mallorquina-", fg = "lightblue", font = ("Time New Roman", 22, "bold italic")).pack()


#Separación de títulos y categorías

Label(root, text ="").pack()

conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()


#Buscar las categorías y platos de bd

categorias = cursor.execute("SELECT * FROM categoria").fetchall()
for categoria in categorias:
    platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
    Label(root, text = categoria[1],fg = "white", font = ("Time New Roman", 15, "bold italic")).pack()
    for plato in platos:
        Label(root, text = plato[1],fg = "gray", font = ("Verdana", 15, "italic")).pack()
         #Separación entre categorías 
    Label(root, text ="").pack()

conexion.close()

#Precio del menú

Label(root, text = "12 euros (IVA incl.)",fg = "black", font = ("Time New Roman", 15, "bold italic")).pack(side = "right")





#Bucle de aplicación 

root.mainloop()