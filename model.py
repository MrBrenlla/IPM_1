#MODEL - GET DATA
import gi
import requests
import threading

from gi.repository import GObject, GLib
GObject.threads_init()

from sys import exit
from random import randint
from html import escape

_error = None
url = "http://127.0.0.1:5000/" #URL/PORT
lNotes= ("do","re♭","re","mi♭","mi","fa","sol♭","sol","la♭","la","si♭","si")

class Data:
    def __init__(self):
        self.notaIni= randint(0,11)
        

class Requests:

    def interval_request(note_name):
        r = Requests.server_request('intervals',True)

        duracion= r.json()['data'][note_name]


        if len(duracion)==2 : 
            return int(duracion[0])*2
        elif len(duracion)==3 : 
            return 1
        else: 
            return int(duracion[0])*2+int(duracion[2])


    def set_error(self,error):
        global _error
        _error = error

    def data_request():

        r = Requests.server_request('intervals',False)
        return r.json()['data'].keys()


    def getSongs(interval,order):

        r = Requests.server_request("songs/"+str(interval)+"/"+str(order),False)
        return r.json()['data']

    def server_request(url_end,bool):

        global url

        try:
            r=requests.get(url+url_end)
        except Exception as e:
            err = _error()
            if bool:
                GLib.idle_add(err.server_error,e,bool)

            else:
                err.server_error(e,bool)
                err.dialog.connect("response",Gtk.main_quit)
                err.dialog.connect("destroy",Gtk.main_quit)
                Gtk.main()
            exit()
        else:
            return r

class Concurrency:
        def create_thread(tg,arg1,arg2):
            x = threading.Thread(target=tg,args=(arg1,arg2))
            x.start()