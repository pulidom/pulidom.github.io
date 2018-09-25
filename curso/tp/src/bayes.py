#!/usr/bin/python
""" 
Bayes rule for inverse problems 

Guia 1 Problema 3

"""
# import library com and load python modules
from com import *

# Domain [-2,4]
nx=100
x=np.linspace(-2,4,nx)

# Observations
sigma_r=0.6
y1=0.5
y2=0.9
y=[y1,y2]

def itema(x): # Gaussian prior
    prior=gauss(x,1,1)
    Hx=dot(ident(x),x)
    return prior, Hx

def itemb(x): # Uniform prior
    prior=unif(x,0,2)
    Hx=dot(ident(x),x)
    return prior, Hx

def itemc(x): # Nonlinear H
    prior=unif(x,0,2)
    Hx=np.sin(np.pi*x)
    return prior, Hx

def posterior(y,sigma_r,prior,Hx):
    " Determine the posterior density using Bayes rule "
    
    # Determine the likelihood function given a realization y
    lik=gauss(y,Hx,sigma_r)

    unnposterior=prior * lik
    marglik=np.sum(unnposterior) #marginal likelihood
    p=unnposterior/marglik # Bayes
    return p

def resolv(x,y,sigma_r,item,pl):
    " Solve each item "
    prior, Hx=item(x)
    p1=posterior(y[0],sigma_r,prior,Hx)
    p2=posterior(y[1],sigma_r,p1,Hx)
    pl.plot_p1_3(x,y,prior,p1,p2)

# Object for plotting
pl=Plot()

# Solve item a
resolv(x,y,sigma_r,itema,pl)

# Solve item b
resolv(x,y,sigma_r,itemb,pl)

# Solve item c
resolv(x,y,sigma_r,itemc,pl)

