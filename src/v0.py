from tkinter import ttk
from v1 import *
from v2 import *
from v4 import *

conexion = sqlite3.connect("bes.db")


class Aplicacion:
    def __init__(self):
        window_main = Tk()

        window_main.title('BES 0.1')
        window_main.config(bg="black")
        window_main.minsize(300, 200)

        top = Frame(window_main)
        top.pack(side=TOP, fill=BOTH)

        middle = Frame(window_main)
        middle.pack(expand=TRUE)

        bottom = Frame(window_main)
        bottom.pack(side=BOTTOM, fill=BOTH)

        b3 = Button(window_main, text='Notificaciones',
                    command=(lambda: v4()))
        b3.pack(in_=top, side=LEFT)

        notificaciones = contar_notificaciones()
        t3 = Label(window_main, text='({0})'.format(notificaciones))
        t3.pack(in_=top, side=LEFT)

        b1 = Button(window_main, text="Requerimientos activos",
                    command=(lambda: v1()))
        b1.pack(in_=middle)

        b2 = Button(window_main, text="Ingresar nuevo requerimiento",
                    command=(lambda: v2()))
        b2.pack(in_=middle)

        b4 = Button(window_main, text='Salir', command=window_main.destroy)
        b4.pack(in_=bottom, side=RIGHT)

        window_main.mainloop()


def contar_notificaciones():
    cursor_notif = conexion.cursor()
    requerimientos = cursor_notif.execute("Select * from REQ001").fetchall()
    cursor_notif.close()
    return len(requerimientos)


def main():
    Aplicacion()
    return 0


if __name__ == '__main__':
    main()
