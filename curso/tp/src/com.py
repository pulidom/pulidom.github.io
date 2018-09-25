import numpy as np
from  numpy import dot
import numpy as np
import numpy.linalg as la
import os
import matplotlib.pyplot as plt
import matplotlib

#------------------------------------------------------
#   Problem 1.3
#------------------------------------------------------
def ident(x):
    return np.eye(x.shape[0])

def gauss(x,mean,sigma):
    #nor=0.5/(np.pi*sigma)
    res = np.exp(-0.5/sigma**2 * (x-mean)**2 )
    res = res/np.sum(res)
    return res

def unif(x,xmin,xmax):
    " Uniform density "
    idx= np.where(x<xmax)
    idx= np.where(x[idx]>xmin)
    res = np.zeros_like(x)
    res[idx] = 1./len(idx[0]) #(xmax-xmin)
    return res

class Plot:
    def __init__(self):
        self.it=0
    def plot_p1_3(self,x,y,prior,p1,p2):
        " Plot the densities "

        self.it=self.it+1
        
        if self.it ==1:
            self.fig = plt.figure(figsize=(9,3))
            self.fig.subplots_adjust(bottom=0.14,top=0.97,right=0.98, \
                                left=0.08,wspace=0.27,hspace=0.2)
            matplotlib.rcParams.update({'legend.frameon' : 0})
            
        
        self.ax1 = self.fig.add_subplot(1,3,self.it)
        if self.it== 1:
            self.ax1.set_ylabel(r'$p$')
        self.ax1.plot(x,prior, label='Prior')
        self.ax1.plot(x,p1, label='Post 1')
        self.ax1.plot(x,p2, label='Post 2')
        self.ax1.plot(y,[0,0],'ro',label='Obs')
        self.ax1.set_xlabel(r'$x$')
        
        if self.it==3:
            self.ax1.legend(loc=0)
            sflroot='tmp/bayes'
            sfl=checkfilename(sflroot)+'-1.eps'
            self.fig.savefig(sfl)
            plt.close(self.fig)
            os.system('checkifrunning '+ sfl)

#------------------------------------------------------
# Other codes
#------------------------------------------------------
def checkfilename(fname):
    """ 
    To avoid overwriting figures:

    Check if the filename exists, and generate a new filename
    """
    #import os
    import glob
    it=1
    while True:
        fnfull=fname+str(it).zfill(2)+'*'#+'-1.eps'
        #os.path.isfile(fnfull)
        #if os.path.isfile(fnfull):
        if glob.glob(fnfull):
            it=it+1
            if it == 100:
                print 'Error! Plot filename limit. Clean tmp/ directory'
                quit()
        else:
            break

    fnroot=fname+str(it).zfill(2)

    return fnroot
