from tkinter import ttk
from v2 import *
from v1 import *


class Aplicacion:
    def __init__(self):
        window_main = Tk()

        window_main.title('BES 0.1')
        window_main.config(bg="black")
        window_main.geometry("300x200")

        b1 = Button(window_main, text="Requerimientos activos",
                    command=(lambda: v1()))
        b1.pack()  # El botón es cargado

        b2 = Button(window_main, text="Ingresar nuevo requerimiento",
                    command=(lambda: v2()))
        b2.pack()  # El botón es cargado

        ttk.Button(window_main, text='Salir', command=window_main.destroy).pack()

        window_main.mainloop()


def main():
    Aplicacion()
    return 0


if __name__ == '__main__':
    main()
