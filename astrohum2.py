#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#PAQUETES EXTERNOS
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
from google.colab import drive,files
from astroquery.vizier import Vizier
import numpy as np

##########################################################
#AQUÍ ESTA LA ROPA SUCIA
##########################################################
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#COMANDOS MAGICOS DE IPYTHON
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
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
