from tkinter import *
from ventanas.notificacion import *
import sqlite3

conexion = sqlite3.connect("bes.db")


def notificaciones():
    ventana_notificaciones = Tk()

    ventana_notificaciones.title('Notificaciones')
    ventana_notificaciones.minsize(300, 200)

    cursor_temp = conexion.cursor()
    query_notificaciones = cursor_temp.execute("Select * from NOTIFICACIONES").fetchall()
    cursor_temp.close()

    for row_notificacion in query_notificaciones:
        boton_notificacion = Button(ventana_notificaciones,
                                    text='Notificacion1',
                                    command=(lambda: notificacion()))
        boton_notificacion.pack()
