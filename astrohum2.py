from google.colab import drive,files
from astroquery.vizier import Vizier
import numpy as np
def matriz(a):
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
