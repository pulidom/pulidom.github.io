#!/usr/bin/python
""" 
Optimal interpolation with two observations

Guia 1 Problema 1

"""
# import library com and load python modules
from com import *

alpha=0.1 #,0.25]

x1=-2.
x0=0.
x2=np.linspace(-4.,4.,100)

d10=abs(x1-x0) 
d12=abs(x1-x2)
d20=abs(x2-x0)
rho10=(1.+d10)*np.exp(-d10)
"""
   Calculate weights for obs 1 and obs 2
"""
rho20=(1+d20)*np.exp(-d20)
rho12=(1+d12)*np.exp(-d12)
w1a=rho10*(1+alpha) - rho12*rho20
w2a=rho20*(1+alpha) - rho12*rho10
denom=(1+alpha)**2-rho12*rho12
w1=w1a/denom
w2=w2a/denom
"""
   Calculate the analysis error variance
     normalized by the background error variance
"""
var_a=1.-((1+alpha)*(rho10**2+rho20**2)-2*rho10*rho20*rho12)/denom

fig = plt.figure(figsize=(4,4))
matplotlib.rcParams.update({'legend.frameon' : 0})
ax1=fig.add_subplot(1,1,1)
ax1.plot(x2,w1, label='w1')
ax1.plot(x2,w2, label='w2')
ax1.plot(x2,var_a, label='analysis var')
ax1.set_xlabel(r'$x/L$')

ax1.legend(loc=0)
sflroot='tmp/opt2obs'
sfl=checkfilename(sflroot)+'-1.eps'
fig.savefig(sfl)
plt.close(fig)
os.system('checkifrunning '+ sfl)
