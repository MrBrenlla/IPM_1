#!/usr/bin/env python3

import gi
import requests
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from random import randint


startNote = 0

notes = None

url = "http://127.0.0.1:5000/" #URL/PORT



lNotes= ("do","re♭","re","mi♭","mi","fa","sol♭","sol","la♭","la","si♭","si")

lDistances= (1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7)


#Main Window

class GUI(Gtk.Window):

    global startNote

    #Initialize GUI

    def __init__(self):
        Gtk.Window.__init__(self,title= "Intervalos")



        #WindowCreation + Properties

        self.set_default_size(500, 200)
        self.set_border_width(30)
        self.set_resizable(False) #Property for can't resize gui window



        #Header

        header = Gtk.HeaderBar(title="Intervalos")
        header.set_subtitle("Seleccione un intervalo")
        header.props.show_close_button = True
        self.set_titlebar(header)



        #FLowBox Creation

        flowbox = Gtk.FlowBox()
        flowbox.set_valign(Gtk.Align.FILL)
        flowbox.set_max_children_per_line(4)

        #flowbox.connect("child-activated", self.on_child_activated)



        #FlowBox properties

        flowbox.set_column_spacing(15)
        flowbox.set_row_spacing(5)
        self.add(flowbox)



        #Get Interval Array

        global notes

        notes = Requests.data_request()
        print(notes)

        #Add elements to FlowBox

        for count in notes:
            label = Gtk.Button(label= count)
            label.connect('clicked', self.on_button_clicked)
            label.set_property("width-request", 50) #Button Size
            label.set_property("height-request", 15) #Button Size
            flowbox.add(label)


    #In case of click on Button

    def on_button_clicked(self, button):

        note_name =  button.get_label()

        print("Interval: " + note_name) #Get name of note

        note_Window = Additional_GUI(note_name)
        note_Window.show_all()



#Notes Window

class Additional_GUI(Gtk.Window):

    #Initialize GUI

    def __init__(self,note):

        Gtk.Window.__init__(self,title= note)
        self.set_default_size(300, 200)
        self.set_border_width(30)


        grid = Gtk.Grid()
        self.add(grid)



        label_Asc = Gtk.Label(label="Ascendente:", xalign=0)
        label_Des = Gtk.Label(label="Descentente:", xalign=0)


        notaIni= randint(0,11)
        distancia=Requests.interval_request(note)
        ascendente=str(lNotes[notaIni])+"-"+str(lNotes[(notaIni+distancia)%12])
        descendente=str(lNotes[notaIni])+"-"+str(lNotes[(notaIni-distancia)%12])
        Additional_GUI.notes_Asc = Gtk.Label(label="Exemplo:"+ascendente, xalign=0)
        Additional_GUI.notes_Des = Gtk.Label(label="Exemplo:"+descendente, xalign=0)



        lb_Asc = Gtk.ListBox()
        lb_Des = Gtk.ListBox()


        songsAsc= Requests.getSongs(note,"asc")

                #Add songs to listbox - ¡Tomar posteriormente las canciones del servidor!

        for i in range(0, len(songsAsc)):

             if songsAsc[i][2]=="YES":
                 text="<a href=\""+songsAsc[i][1]+"\" > <b> "+songsAsc[i][0]+" </b></a>"
             else:
                text="<a href=\""+songsAsc[i][1]+"\" > "+songsAsc[i][0]+" </a>"

             song = Gtk.Label()
             song.set_markup(text)


             lb_Asc.add(song)


        songsDes= Requests.getSongs(note,"des")

        for i in range(0, len(songsDes)):

            if songsDes[i][2]=="YES":
                text="<a href=\""+songsDes[i][1]+"\" > <b> "+songsDes[i][0]+" </b></a>"
            else:
                text="<a href=\""+songsDes[i][1]+"\" > "+songsDes[i][0]+" </a>"

            song = Gtk.Label()
            song.set_markup(text)


            lb_Des.add(song)


        #Grid properties

        grid.set_column_spacing(30)
        grid.set_row_spacing(10)

        #Grid elements

        label_Asc.set_hexpand(True)
        label_Des.set_hexpand(True)

        grid.add(label_Asc)
        grid.attach(label_Des, 1, 0, 2, 1)
        grid.attach_next_to(Additional_GUI.notes_Asc, label_Asc, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(Additional_GUI.notes_Des, label_Des, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(lb_Asc, Additional_GUI.notes_Asc, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(lb_Des, lb_Asc, Gtk.PositionType.RIGHT, 1, 1)



class Requests():

    global url


    def interval_request(note_name):

        #r = requests.get('http://127.0.0.1:5000/intervals')
        #NOTE-DATA REQUEST

        r = requests.get(url+'intervals')

        #DATA -> KEY

        duracion= r.json()['data'][note_name]


        if len(duracion)==2 : #Forma _T
            return int(duracion[0])*2
        elif len(duracion)==3 : #1ST é o único caso con 3 letras
            return 1
        else: #forma _T_ST
            return int(duracion[0])*2+int(duracion[2])



    def data_request():

        r = requests.get(url+'intervals')
        print(r.json()['data'].keys())
        return r.json()['data'].keys()


    def getSongs(interval,order):

        r = requests.get(url+"songs/"+str(interval)+"/"+str(order))
        return r.json()['data']


window = GUI()
window.connect("destroy", Gtk.main_quit) #In case of window exit
window.show_all()
Gtk.main()
