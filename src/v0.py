from tkinter import *
from tkinter import ttk
import funciones
from v1 import *
from v2 import *
from v1 import *

print('hola munco')


class Aplicacion():
    def __init__(self):
        v0 = Tk()
        #v0.geometry('300x200')
        v0.configure(bg='beige')
        v0.title('BES 1.0')


        def ejecutar(f): v0.after(200, f)

        v0.config(bg="black")  # Le da color al fondo
        v0.geometry("500x500")  # Cambia el tamaño de la ventana

        b1 = Button(v0, text="Requerimientos activos",
                    command=(lambda: v1()))  # Primer botón
        b1.pack()  # El botón es cargado
        b2 = Button(v0, text="Ingresar nuevo requerimiento",
                    command=(lambda: v2()))  # Primer botón
        b2.pack()  # El botón es cargado
        b3 = Button(v0, text="Boton 3",
                    command=lambda:print("botn 3"))  # Primer botón
        b3.pack()  # El botón es cargado

        ttk.Button(v0, text='Salir', command=v0.destroy).pack()
        # archivo-entrada.py
        f = open("pruet.txt")
        mensaje = f.read()
        print(mensaje)

        v0.mainloop()


def main():
    mi_app = Aplicacion()
    return 0


if __name__ == '__main__':
    main()
