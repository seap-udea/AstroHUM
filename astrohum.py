#-*- coding: utf-8 -*-
#########################################
#Aquí esta la ropa limpia
#########################################
from google.colab import drive,files

#########################################
#Aquí esta la ropa sucia
#########################################
#Comandos mágicos de Colaboratory
from IPython.core.magic import (register_line_magic, register_cell_magic,
                                register_line_cell_magic)
@register_line_magic
def upload(line):
    files.upload()
del upload

@register_line_magic
def mount(line):
    drive.mount('/content/gdrive')
del mount


