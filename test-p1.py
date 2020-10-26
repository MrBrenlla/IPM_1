#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import textwrap
from collections import namedtuple
from time import sleep

import gi
gi.require_version('Atspi', '2.0')
from gi.repository import Atspi

import e2e

print('\033[91m', "Esta proba está pensada para facela en es_ES.utf-8,\n ainda que tanto en_US.utf-8 como gl_ES.utf-8 son\n soportadas por ipm-p1.py estas configuracións non \n pasarán este test.\n\n", '\033[0m')

"""Histories:
    GIVEN he lanzado la aplicación
    THEN vel el botón "3M"
    GIVEN he lanzado la aplicación
    WHEN pulso el botón '3M'
    THEN veo la ventana '3M'
    GIVEN he lanzado la aplicación
    WHEN pulso el botón '3M'
    THEN veo la ventana '3M'
    THEN veo el texto "Ascendente:"
    GIVEN he lanzado la aplicación
    WHEN pulso el botón '3M'
    THEN veo la ventana '3M'
    THEN veo el texto "Ascendente:"
    THEN veo el text "Exemplo:+intervalo"
"""

# Funciones de ayuda

def show(text):
    print(textwrap.dedent(text))

def show_passed():
    print('\033[92m', "    Passed", '\033[0m')

def show_not_passed(e):
    print('\033[91m', "    Not passsed", '\033[0m')
    print(textwrap.indent(str(e), "    "))


# Contexto de las pruebas

Ctx = namedtuple("Ctx", "path process app")


# Implementación de los pasos

def given_he_lanzado_la_aplicacion(ctx):
    process, app = e2e.run(ctx.path)
    assert app is not None
    return Ctx(path= ctx.path, process= process, app= app)

def when_pulso_el_boton_3M(ctx):
    gen = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'push button' and node.get_name() == '3M')
    boton = next(gen, None)
    assert boton is not None
    e2e.do_action(boton, 'click')
    return ctx

def then_veo_la_ventana_3M(ctx):
    sleep(2) #Esperamos por se a pantalla ainda non cargou
    gen = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'frame' and node.get_name() == '3M')
    frame = next(gen, None)
    assert frame and frame.get_name() == "3M", frame.get_text()
    #print("NAME OF FRAME: " + frame.get_name()) #Nombre de la nueva ventana
    return ctx

def then_veo_el_texto_asc(ctx):
    gen = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'label' and node.get_text(0, -1).startswith("Ascendente"))
    label = next(gen, None)
    assert label and label.get_text(0, -1) == "Ascendente:", label.get_text(0, -1)
    #print("LABEL TEXT: " + label.get_text(0, -1))
    return ctx

def then_interv_asc_novacio(ctx):
    gen = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'label' and node.get_text(0, -1).startswith("Ejemplo:"))
    label = next(gen, None) #Ventana des
    label = next(gen, None) #Ventana asc
    text_size= len("Exemplo:")
    assert label and len(label.get_text(0, -1)) > text_size, label.get_text(0, -1)
    #print("LABEL TEXT: " + label.get_text(0, -1))
    return ctx

if __name__ == '__main__':
    sut_path = sys.argv[1]
    initial_ctx = Ctx(path= sut_path, process= None, app= None)

    show("""
    GIVEN he lanzado la aplicación
    THEN pulso el botón "3M"
    """)
    ctx = initial_ctx
    try:
        ctx = given_he_lanzado_la_aplicacion(ctx)
        ctx = when_pulso_el_boton_3M(ctx)
        show_passed()
    except Exception as e:
        show_not_passed(e)
    e2e.stop(ctx.process)

    show("""
    GIVEN he lanzado la aplicación
    WHEN pulso el botón '3M'
    THEN veo la ventana '3M'
    """)
    ctx = initial_ctx
    try:
        ctx = given_he_lanzado_la_aplicacion(ctx)
        ctx = when_pulso_el_boton_3M(ctx) #Cuando pulso 3M
        ctx = then_veo_la_ventana_3M(ctx) #Veo la ventana 3M
        show_passed()
    except Exception as e:
        show_not_passed(e)
    e2e.stop(ctx.process)

    show("""
    GIVEN he lanzado la aplicación
    WHEN pulso el botón '3M'
    THEN veo la ventana '3M'
    THEN veo el texto "Ascendente:"
    """)
    ctx = initial_ctx
    try:
        ctx = given_he_lanzado_la_aplicacion(ctx)
        ctx = when_pulso_el_boton_3M(ctx) #Cuando pulso 3M
        ctx = then_veo_la_ventana_3M(ctx) #Veo la ventana 3M
        ctx = then_veo_el_texto_asc(ctx) #Veo el texto
        show_passed()
    except Exception as e:
        show_not_passed(e)
    e2e.stop(ctx.process)

    show("""
    GIVEN he lanzado la aplicación
    WHEN pulso el botón '3M'
    THEN veo la ventana '3M'
    THEN veo el texto "Ascendente:"
    THEN veo el text "Exemplo:+intervalo"
    """)
    ctx = initial_ctx
    try:
        ctx = given_he_lanzado_la_aplicacion(ctx)
        ctx = when_pulso_el_boton_3M(ctx) #Cuando pulso 3M
        ctx = then_veo_la_ventana_3M(ctx) #Veo la ventana 3M
        ctx = then_veo_el_texto_asc(ctx) #Veo el texto
        ctx = then_interv_asc_novacio(ctx) #Veo el intervalo - no vacío
        show_passed()
    except Exception as e:
        show_not_passed(e)
    e2e.stop(ctx.process)
