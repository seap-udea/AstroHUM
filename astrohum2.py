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

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#RUTINAS NUMERICAS
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def matriz(a):
    """
    Convierte un arreglo estructurado en un arreglo plano
    """
    import numpy as np
    a=np.array(a)
    dt = a.dtype
    dt = dt.descr
    nt=[]
    for t in dt:
        t = (t[0], 'float64')
        nt+=[t]
    dt = np.dtype(nt)
    a = a.astype(dt)
    a=a.view(np.float).reshape(a.shape + (-1,))
    return a

def sex2dec(s):
    """
    Convierte un ángulo expresado en sexagesimal a su expresión en decimal.

    Ejemplo: sex2dec("23 03 45") devuelve 23.0625
    """
    d=np.sign(float(s.split()[0]))*(np.array([np.abs(float(x)) for x in s.split()]).dot([1.0,1/60.0,1/3600.]).sum())
    return d

def dec2sex(d,fmt="list",sep=" "):
    s=np.sign(d)
    d=np.abs(d)
    dg=int(d)
    mm=(d-dg)*60
    mg=int(mm)
    sg=(mm-mg)*60
    sex=None
    if fmt=="list":
        sex=s*dg,mg,sg
    if fmt=="string":
        sex="%02d%s%02d%s%02.2f"%(s*dg,sep,mg,sep,sg)
    return sex
