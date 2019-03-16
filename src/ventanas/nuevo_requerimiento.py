#Ventana de nuevo requerimiento

from tkinter import *
import sqlite3
import json

conexion = sqlite3.connect("bes.db")

cursor = conexion.cursor()
#cursor.execute("CREATE TABLE REQ001(ID  NUMERIC(5) , TITULO CHAR(80), DESCRIP VARCHAR(1000))")

editable = "normal"
def requerimientos():
    v2 = Tk()
    v2.title('Nuevo requerimiento')
    v2.resizable(1,1)
    v2.configure(bg = 'beige')



    nombre = Label(v2, text="Ingrese título")
    nombre.configure( fg="black", )
    nombre.pack()
    t1 = Entry(v2)
    t1.config( fg="black", state=editable)
    t1.pack()
    descripcion = Label(v2, text="Descripción")
    descripcion.pack()
    descritxt = Text(v2)

    descritxt.config(width=80, height=10)
    descritxt.pack()


    b1 = Button(v2, text="Guardar",
                command=lambda:guardar(t1.get(), descritxt.get("1.0", END)))  # Primer botón
    print(editable)
    b1.pack()  # El botón es cargado
    #b2 = Button(v2, text="Editar",
    #            command=lambda: editar(t1))  # Primer botón



    v2.mainloop()

def guardar(titulo, descripcion):
    identidad = 1
    cursor.execute("SELECT id FROM REQUERIMIENTOS ORDER BY ID DESC")
    idsiguiente = cursor.fetchone()
    if idsiguiente is not None:
        identidad = idsiguiente[0] + 1

    print(identidad)
    cursor.execute("Insert into REQUERIMIENTOS (id, titulo, estado) values({}, '{}', 1)".format(identidad, titulo ))
    f = open("{}.txt".format(identidad), "w")
    f.write(descripcion)
    f.close()


    data = {}
    data['entrada'] = []
    data['entrada'].append({
        'texto' : '{}'.format(descripcion),
        'autor'  : 'Fernando',
        'cliente' : 'SI'
    })
    with open("{}.json".format(identidad), 'w') as outfile:
        json.dump(data, outfile)


    #titulo = t1get
    print(titulo)
    print(descripcion)
    print("boton guardar")
    conexion.commit()
    #cambEst("ne", cuadro, b2)
#def cambEst(par1, cuadro)#, b2):
#    if (par1 == "ne"): #no editable
#        editable = "readonly"
#        cuadro.config(state=editable)
#        print("Cambio estado")
#        b2.pack()

def editar(cuadro):
    cuadro.config(state="normal")






