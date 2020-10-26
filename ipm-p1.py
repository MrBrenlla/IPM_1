#!/usr/bin/env python3

from controller import Controller
import model
import view

if __name__ == '__main__':

    controller = Controller()
    controller.set_model(model)
    controller.set_view(view.View())
    controller.set_error(view)
    controller.main()
