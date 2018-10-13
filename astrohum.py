#-*- coding: utf-8 -*-
##########################################################
#AQUÍ ESTA LA ROPA LIMPIA
##########################################################

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#PAQUETES EXTERNOS
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#Colaboratory
from google.colab import drive,files

#Paquetes numericos
import numpy as np

#Astropy
from astropy.io import fits
from astropy.coordinates import Angle

#Astroquery
from astroquery.vizier import Vizier

#Paquetes graficos
import matplotlib.pyplot as plt

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#RUTINAS
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def fuentes(img,fwhm=3.0,umbral=5.0):
    """
    Extrae las fuentes de una imagen
    """
    from astropy.stats import sigma_clipped_stats
    from photutils import DAOStarFinder
    mean,median,std=sigma_clipped_stats(img,sigma=3.0,iters=5)
    daofind=DAOStarFinder(fwhm=fwhm,threshold=umbral*std)
    sources=daofind(img-median)
    return sources

def convertidor(info):
    from astropy import wcs
    w=wcs.WCS(naxis=2)
    w.wcs.crpix=np.array([info["CRPIX1"],info["CRPIX2"]])
    w.wcs.cdelt=np.array([info["CDELT1"],info["CDELT2"]])
    w.wcs.crval=np.array([info["CRVAL1"],info["CRVAL2"]])
    w.wcs.ctype=[info["CTYPE1"],info["CTYPE2"]]
    c=lambda x:w.wcs_pix2world(x,0)
    return c

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
#RUTINAS NUMÉRICAS
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
