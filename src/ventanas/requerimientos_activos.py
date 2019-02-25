# Lista requerimientos activos, es llamada por principal

from tkinter.tix import Tk
from ventanas.requerimiento import *

conexion = sqlite3.connect("bes.db")


def requerimientos_activos():
    window_reqs = Tk()
    window_reqs.title('Requerimientos activos')
    window_reqs.minsize(300, 200)

    cursor_temp = conexion.cursor()
    query_requerimientos = cursor_temp.execute("Select * from REQUERIMIENTOS").fetchall()
    cursor_temp.close()

    lista_requerimientos = Listbox(window_reqs,
                                   selectmode=SINGLE)
    lista_requerimientos.pack()

    for requerimiento in query_requerimientos:
        nombre_req = '{0} - {1}'.format(requerimiento[0], requerimiento[1])
        lista_requerimientos.insert(END, nombre_req)

    Button(window_reqs,
           text='Seleccionar requerimiento',
           command=(lambda: requerimiento(query_requerimientos[lista_requerimientos.curselection()[0]]))).pack()
