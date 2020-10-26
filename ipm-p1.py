#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from controller import Controller
import model
import view
import locale
import gettext
from pathlib import Path

locale.setlocale(locale.LC_ALL,'')

locale.bindtextdomain("ipm-p1",Path(__file__).parent / "locale")
gettext.bindtextdomain("ipm-p1",Path(__file__).parent / "locale")
gettext.textdomain("ipm-p1")

if __name__ == '__main__':

    controller = Controller()
    controller.set_model(model)
    controller.set_view(view.View())
    controller.set_error(view)
    controller.main()

