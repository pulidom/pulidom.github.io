#----------------------------------------------------------    
def rk4(mdl,xold):
    """ Runge-Kutta 4th order (time independent)
       mdl es el modelo multiplado por dt 
       dx/dt= x^2+a x --> mdl=dt*(x^2+a * x)
    """

    dx1 = mdl( xold )
    dx2 = mdl( xold + 0.5 * dx1 )
    dx3 = mdl( xold + 0.5 * dx2 )
    dx4 = mdl( xold + dx3 )

    x = xold +  ( dx1 + 2.0 * (dx2 + dx3) + dx4 ) / 6.0

    return x 
