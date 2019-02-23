# Lista requerimientos activos, es llamada por v0

from tkinter import ttk, Button
import sqlite3
from tkinter.tix import Tk
from v3 import *
conexion = sqlite3.connect("bes.db")
cursor = conexion.cursor()
def v1():
    v1 = Tk()
    v1.title('Requerimientos activos')
    v1.geometry('500x200')

    requerimientos = cursor.execute("Select * from REQ001").fetchall()
    # self.button =[]
    for requerimiento in requerimientos:  # recorro los requerimientos guardados en la BD y para cada uno creo un botón
        print(requerimiento[1])
        id = requerimiento[0]
        # self.button.append
        Button(v1, text=requerimiento[1], command=(lambda: v3(id))).pack()  # Primer botón
