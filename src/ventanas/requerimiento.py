from tkinter import *
import sqlite3
import json

conexion = sqlite3.connect("bes.db")
cursor = conexion.cursor()
global veces
def requerimiento(id):
        id = id[0]
        cursor.execute("select TITULO from REQUERIMIENTOS where id = {}".format(id))
        titulo = cursor.fetchone()
        titulo = titulo[0]
        print(titulo)
        v3 =  Tk()
        v3.title('Req: '+str(id)+' ' + titulo)
        #v3.geometry('500x200')
        #v3.minsize(300,200)

        scrollbar = Scrollbar(v3)
        canvas = Canvas(v3, background='pink', yscrollcommand=scrollbar.set)
        scrollbar.config(command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        frame = Frame(canvas)
        frame.config(bg='blue')

        canvas.pack(side='left', fill='both', expand=True)
        canvas.create_window(0,0, window=frame, anchor='nw')

        cargarentr(frame, id)
        v3.update()
        canvas.config(scrollregion=canvas.bbox("all"))

        v3.mainloop()


def cargarentr(frame, id):
    cursor.execute("select * from REQUERIMIENTOS where id = {}".format(id))
    with open('{}.json'.format(id)) as file:
        entradas = json.load(file)
        print(entradas)
        data = {}
        data['entrada'] = []

        for entrada in entradas['entrada']:
            justifiacar = 'right '
            if entrada['cliente'] == 'SI':
                justifiacar = 'left'
            label1 = Label(frame, text=entrada['texto'])
            label1.config(justify= "left")
            respuesta = entrada['texto']
            label1.pack()
            data['entrada'].append({
                'texto': '{}'.format(respuesta),
                'autor': 'Fernando',
                'cliente': 'SI'#***********************************************
            })

    crearCuadro(id, frame, data)

def guardar(boton,id,frame,cuadro, respuesta, data):
    respuesta = respuesta.strip()
    print('respuesta:'+respuesta+'.')
    if respuesta != '':
        data['entrada'].append({
            'texto': '{}'.format(respuesta),
            'autor': 'Fernando',
            'cliente': 'SI'
        })
        with open("{}.json".format(id), 'w') as outfile:
            json.dump(data, outfile)

        cuadro.destroy()
        boton.destroy()
        Label(frame, text =respuesta).pack()
        crearCuadro(id, frame, data)

def crearCuadro(id, frame, data):
    respuesta = Text(frame, width=(50), height="5")

    contestar = Button(frame, text=("Responder"), command=(lambda: guardar( contestar,id, frame,respuesta, respuesta.get('1.0', END), data)))
    respuesta.pack()
    contestar.pack()