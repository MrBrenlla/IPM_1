#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import model
import gi
import requests
import threading
import os
import time
import gettext

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, GLib
GObject.threads_init()

from sys import exit
from random import randint
from html import escape

_ = gettext.gettext


class View(Gtk.Window):

    button_name= None

    __gsignals__ = {
        'button-clicked': (GObject.SIGNAL_RUN_FIRST, None, ())
    }


    def main(cls):
        Gtk.main()

    def main_quit(cls,w,e):
        Gtk.main_quit()

    def build_view(self):

        self.wndw = Gtk.Window(title= _("Intervalos"))

        #WindowCreation + Properties
        self.wndw.set_default_size(500, 200)
        self.wndw.set_border_width(30)
        self.wndw.set_resizable(False) #Property for can't resize gui window



        #Header
        header = Gtk.HeaderBar(title=_("Intervalos"))
        header.set_subtitle(_("Seleccione un intervalo"))
        header.props.show_close_button = True
        self.wndw.set_titlebar(header)



        #FLowBox Creation
        flowbox = Gtk.FlowBox()
        flowbox.set_valign(Gtk.Align.FILL)
        flowbox.set_max_children_per_line(4)


        #FlowBox properties
        flowbox.set_column_spacing(15)
        flowbox.set_row_spacing(5)
        self.wndw.add(flowbox)

        notes = model.Requests.data_request()
        for count in notes:
            label = Gtk.Button(label= count)
            label.connect('clicked', self.connect_button_clicked)
            label.set_property("width-request", 50)
            label.set_property("height-request", 15)
            flowbox.add(label)

    def window_secondary_view(note):
        return Gtk.Window(title= note)

    def build_secondary_view(self,note,win):

        notaInicial = model.Data().notaIni
        distancia= model.Requests.interval_request(note)
        ascendente= _(str(model.lNotes[notaInicial]))+"-"+_(str(model.lNotes[(notaInicial+distancia)%12]))
        descendente= _(str(model.lNotes[notaInicial]))+"-"+_(str(model.lNotes[(notaInicial-distancia)%12]))

        win.set_default_size(300, 200)
        win.set_border_width(30)

        grid = Gtk.Grid()
        win.add(grid)

        label_Asc = Gtk.Label(label=_("Ascendente:"), xalign=0)
        label_Des = Gtk.Label(label=_("Descentente:"), xalign=0)

        notes_Asc = Gtk.Label(label=_("Exemplo:")+ascendente, xalign=0)
        notes_Des = Gtk.Label(label=_("Exemplo:")+descendente, xalign=0)

        lb_Asc = Gtk.ListBox()
        lb_Des = Gtk.ListBox()

        songsAsc= model.Requests.getSongs(note,"asc")

        for i in range(0, len(songsAsc)):

             if songsAsc[i][2]=="YES":
                text="<a href=\""+escape(songsAsc[i][1])+"\" > <b> "+songsAsc[i][0]+" </b></a>"
             else:
                text="<a href=\""+escape(songsAsc[i][1])+"\" > "+songsAsc[i][0]+" </a>"

             escape(text, quote=True)

             song = Gtk.Label()
             song.set_markup(text)


             lb_Asc.add(song)


        songsDes= model.Requests.getSongs(note,"des")

        for i in range(0, len(songsDes)):

            if songsDes[i][2]=="YES":
                text="<a href=\""+escape(songsDes[i][1])+"\" > <b> "+songsDes[i][0]+" </b></a>"
            else:
                text="<a href=\""+escape(songsDes[i][1])+"\" > "+songsDes[i][0]+" </a>"


            escape(text, quote=True)
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
        grid.attach_next_to(notes_Asc, label_Asc, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(notes_Des, label_Des, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(lb_Asc, notes_Asc, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(lb_Des, lb_Asc, Gtk.PositionType.RIGHT, 1, 1)


        GLib.idle_add(self.show_secondary_all,win)

    def show_all(self):
        self.wndw.show_all()

    def connect_delete_event(self, fun):
        self.wndw.connect('delete-event', fun)

    def show_secondary_all(self,win):
        win.show_all()

    def connect_button_clicked(self, button, *args):

        self.set_button_name(button.get_label())
        self.emit('button-clicked')

    def set_button_name(self,button):
        global button_name
        button_name = button

    def get_button_name(self):
        return button_name



class error:

    dialog=None

    def server_error(self, e,bool):
        text= _("Error inesperado:\n")+ escape(str(e))
        self.dialog = Gtk.Dialog()
        self.dialog.set_title("Error")
        self.dialog.set_modal(True)
        self.dialog.add_button(button_text="OK",response_id=0)
        content_area = self.dialog.get_content_area()
        label = Gtk.Label(text)
        content_area.add(label)
        self.dialog.show_all()
        if bool:
            self.dialog.connect("response",self.end)

    def end(self,a,b):
        self.dialog.destroy()
