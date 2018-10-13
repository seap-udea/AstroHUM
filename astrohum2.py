#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#PAQUETES EXTERNOS
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
from google.colab import drive,files
from astroquery.vizier import Vizier
import numpy as np

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
