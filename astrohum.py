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

@register_upload
def upload(line):
    files.upload()
    
del upload
