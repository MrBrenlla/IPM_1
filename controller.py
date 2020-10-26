import model
import view

import gi
import requests

from sys import exit
from random import randint
from html import escape

class Controller:

    def set_model(self, model):
        self.model = model
        
    def set_view(self, view):
        self.view = view
        view.build_view()
        view.connect_delete_event(self.view.main_quit)
        self.view.connect('button-clicked',self.on_button_clicked)
   
    def set_error(self,view):
        self.model.Requests.set_error(view.error,view.error)

    def main(self):
        self.view.show_all()
        self.view.main()


    def set_secondary_view(self,note):
        self.win = view.View.window_secondary_view(note)
        model.Concurrency.create_thread(self.view.build_secondary_view,note,self.win)       

    def on_button_clicked(self,button,*args):
        note = str(self.view.get_button_name())
        self.set_secondary_view(note)
