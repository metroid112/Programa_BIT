from tkinter import *
import sqlite3
import json

conexion = sqlite3.connect("bes.db")
cursor = conexion.cursor()
global veces
def v3(id):
        id = id[0]

        v3 =  Tk()
        v3.title('Requerimiento: '+str(id))
        #v3.geometry('500x200')
        v3.minsize(300,200)

        cargarentr(v3, id)

        v3.mainloop()


def cargarentr(v3, id):
    cursor.execute("select * from req001 where id = {}".format(id))
    #entradas = cursor.fetchall()
    #print('entradas: ' + str(entradas[0]))
   # for entrada in entradas:
    #    veces = entrada[5]
    #    print(veces)
    with open('{}.json'.format(id)) as file:
        entradas = json.load(file)
        print(entradas)
        data = {}
        data['entrada'] = []

        for entrada in entradas['entrada']:
            label1 = Label(v3, text=entrada['texto'])
            respuesta = entrada['texto']
            label1.pack()
            data['entrada'].append({
                'texto': '{}'.format(respuesta),
                'autor': 'Fernando'
            })




    crearCuadro(id, v3, data)




def guardar(boton,id,v3,cuadro, respuesta, data):

    data['entrada'].append({
        'texto': '{}'.format(respuesta),
        'autor': 'Fernando'
    })
    with open("{}.json".format(id), 'w') as outfile:
        json.dump(data, outfile)

    cuadro.destroy()
    boton.destroy()
    Label(v3, text =respuesta).pack()
    crearCuadro(id, v3, data)

def crearCuadro(id, v3, data):
    respuesta = Text(v3, width=(50), height="5")

    contestar = Button(v3, text=("Responder"), command=(lambda: guardar( contestar,id, v3,respuesta, respuesta.get('1.0', END), data)))
    respuesta.pack()
    contestar.pack()