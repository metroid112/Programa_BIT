# Lista requerimientos activos, es llamada por v0

import sqlite3
from tkinter.tix import Tk
from v3 import *


def v1():
    window_reqs = Tk()
    window_reqs.title('Requerimientos activos')
    window_reqs.minsize(300,200)

    conexion = sqlite3.connect("bes.db")
    cursor = conexion.cursor()
    requerimientos = cursor.execute("Select * from REQ001").fetchall()
    cursor.close()

    lista_req = Listbox(window_reqs, selectmode=SINGLE)
    lista_req.pack()

    for requerimiento in requerimientos:  # recorro los requerimientos guardados en la BD y para cada uno creo un botón
        print(requerimiento[1])
        print(requerimiento[0])
        nombre_req = '{0} - {1}'.format(requerimiento[0], requerimiento[1])
        lista_req.insert(END, nombre_req)

    print(requerimientos)
    Button(window_reqs, text='Seleccionar requerimiento', command=(lambda: v3(
        requerimientos[lista_req.curselection()[0]]
    ))).pack()
