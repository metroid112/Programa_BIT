# Ventana principal (main)
from ventanas.requerimientos_activos import *
from ventanas.nuevo_requerimiento import *
from ventanas.notificaciones import *
from ventanas.busqueda import *

conexion = sqlite3.connect("bes.db")


class Aplicacion:
    def __init__(self):
        ventana_principal = Tk()

        ventana_principal.title('BES 0.4')
        ventana_principal.config(bg="black")
        ventana_principal.minsize(300, 200)

        # FRAMES #
        tope = Frame(ventana_principal)
        tope.pack(side=TOP,
                  fill=BOTH)

        medio = Frame(ventana_principal)
        medio.pack(expand=TRUE)

        debajo = Frame(ventana_principal)
        debajo.pack(side=BOTTOM,
                    fill=BOTH)

        # BOTON NOTIFICACION #
        boton_notificaciones = Button(ventana_principal,
                                      text='Notificaciones',
                                      command=(lambda: notificaciones()))
        boton_notificaciones.pack(in_=tope,
                                  side=LEFT)

        # CONTADOR NOTIFICACION #
        numero_notificaciones = contar_notificaciones()
        contador_notificaciones = Label(ventana_principal,
                                        text='({0})'.format(numero_notificaciones))
        contador_notificaciones.pack(in_=tope, side=LEFT)


        # BUSCADOR REQ ACTIVOS #
        busqueda_requerimientos = StringVar()
        buscador_requerimientos = Entry(ventana_principal,
                                        textvariable=busqueda_requerimientos)

        boton_buscador = Button(ventana_principal,
                                text='Buscar',
                                command=(lambda: busqueda(busqueda_requerimientos.get())))

        boton_buscador.pack(in_=tope, side=RIGHT)
        buscador_requerimientos.pack(in_=tope, side=RIGHT)

        # CONTADOR REQ ACTIVOS #
        boton_requerimientos_activos = Button(ventana_principal,
                                              text="Requerimientos activos",
                                              command=(lambda: requerimientos_activos()))
        boton_requerimientos_activos.pack(in_=medio)

        # CONTADOR REQ NUEVO #
        boton_requerimiento_nuevo = Button(ventana_principal,
                                           text="Ingresar nuevo requerimiento",
                                           command=(lambda: requerimientos()))
        boton_requerimiento_nuevo.pack(in_=medio)

        # BOTON SALIR #
        boton_salir = Button(ventana_principal,
                             text='Salir',
                             command=ventana_principal.destroy)
        boton_salir.pack(in_=debajo,
                         side=RIGHT)

        # LOOP PRINCIPAL #
        ventana_principal.mainloop()


def contar_notificaciones():
    cursor_temp = conexion.cursor()
    query_notificaciones = cursor_temp.execute("Select * from NOTIFICACIONES").fetchall()
    cursor_temp.close()
    return len(query_notificaciones)


def main():
    Aplicacion()
    return 0


if __name__ == '__main__':
    main()
