from tkinter import *


def v3(req):
    window_req = Tk()
    req_title = 'Requerimiento: {0}'.format(req[0])
    window_req.title(req_title)
    window_req.minsize(300, 200)
    window_req.mainloop()
