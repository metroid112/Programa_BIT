from tkinter import *
from ventanas.requerimiento import *
import sqlite3

conexion = sqlite3.connect("bes.db")


def busqueda(busqueda_requerimientos):
    ventana_busqueda = Tk()

    ventana_busqueda.title('Busqueda')
    ventana_busqueda.minsize(300, 200)

    busqueda_requerimientos = '%' + busqueda_requerimientos + '%'

    cursor_temp = conexion.cursor()
    busqueda_requerimientos = (busqueda_requerimientos, )
    cursor_temp.execute("Select * from REQUERIMIENTOS where TITULO like ? and ESTADO = 1", busqueda_requerimientos)
    query_requerimientos = cursor_temp.fetchall()
    cursor_temp.close()

    lista_requerimientos = Listbox(ventana_busqueda,
                                   selectmode=SINGLE)
    lista_requerimientos.pack()

    for row_requerimiento in query_requerimientos:
        nombre_req = '{0} - {1}'.format(row_requerimiento[0], row_requerimiento[1])
        lista_requerimientos.insert(END, nombre_req)

    Button(ventana_busqueda,
           text='Seleccionar requerimiento',
           command=(lambda: requerimiento(query_requerimientos[lista_requerimientos.curselection()[0]]))).pack()
