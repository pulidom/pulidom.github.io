#!/usr/bin/python
""" 
Covariance matrix of the background

Guia 1 Problema 2

"""
# import library com and load python modules
from com import *

nx=100
ny=1
Ld=0.2
Lx=1.0 
R=1.0 * np.eye(ny) # error de la obs
H=np.zeros(nx)          #operador observation
jy=25
H[jy]=1.0


def corr(Ld,Lx,nx):
    # Correlation
    Ix1=np.linspace(0,Lx,nx+1) # without the boundaries?
    # remove start point
    Ix1=Ix1[1:]
    Ix2=Ix1

    [I1,I2]=np.meshgrid(Ix1,Ix2)
    #Idiff   = abs(I1-I2)
    #Rho = (1+Idiff/Ld) * np.exp(-Idiff/Ld) #soar
    
    Rho = np.exp(-0.5*dot((I1-I2).T,I1-I2)/Ld**2) #gaussian

    return Rho

def autov(Rho):
    # Determine eigenvalues and eigenvectors of the correlation
    s, V = la.eig(Rho)

    # ordena los autovalores
    idx = sA.argsort()[: : -1]
    sA = sA[idx]
    VA = VA[:,idx]

    return sA,VA


def itemb(sRho,VRho,sigmab):
    """
    La idea de este item es no solo calcular con los autovalores y autovectores 
    pero darse cuenta que los autovalores son la transformada de Fourier
    de la funcion de correlacion y por lo tanto no es necesario hacer SVD en sistemas
    grandes
    """
    sqrts=np.sqrt(s)*sigmab
    n = np.size(s)
    sqrtS = np.zeros((n,n))
    sqrtS[:n, :n] = np.diag(sqrts)
      
    sqrtB=dot(VB,dot(sqrtS, VB.T))

    # Alternative
    # transformar en Fourier (autofnes) a Rho y luego usar a estos como autovalores
    # y las autofunciones
    
    return

def itemc():
    """

    """
    return
