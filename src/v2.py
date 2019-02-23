#Ventana de nuevo requerimiento

from tkinter import *
import sqlite3

conexion = sqlite3.connect("bes.db")

cursor = conexion.cursor()
#cursor.execute("CREATE TABLE REQ001(ID  NUMERIC(5) , TITULO CHAR(80), DESCRIP VARCHAR(1000))")

editable = "normal"
def v2():
    v2 = Tk()
    v2.title('Nuevo requerimiento')

   # v2.geometry('500x200')
    v2.resizable(1,1)
    v2.configure(bg = 'beige')
    #frame = Frame(v2)
    #frame.pack()
   # frame.config(cursor = "Pirate", width=100, height = 100, bg = "black")

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
    cursor.execute("SELECT id FROM REQ001 ORDER BY ID DESC")
    idsiguiente = cursor.fetchone()
    print(idsiguiente[0])
    idsiguiente = idsiguiente[0] + 1
    cursor.execute("Insert into REQ001 (id, titulo) values({}, '{}')".format(idsiguiente, titulo ))
    f = open("{}.txt".format(idsiguiente), "w")
    f.write(descripcion)
    f.close()
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






