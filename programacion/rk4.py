#- 3 -------------------------------------------------
    def rk4(x,mdl):
        " 4th order Runge Kutta. Asume que mdl esta multiplicado por el paso del tiempo "
        
        xtmp = x
        dxf1 = mdl(xtmp)
        
        xtmp = x + 0.5 * dxf1
        dxf2 = mdl(xtmp)

        xtmp = x + 0.5 * dxf2
        dxf3 = mdl(xtmp)
        
        xtmp = x + dxf3
        dxf4 = mdl(xtmp)

        x = x +  ( dxf1 + 2.0 * dxf2 + 2.0 * dxf3 + dxf4 ) / 6.0
        return x
#- 3 -------------------------------------------------
    def df(x,mdl):
        " Diferencia finita. Asume que mdl esta multiplicado por el paso del tiempo "
        
        dx= mdl(x) # dt is incorporated in the model

        x = x +  dx
        return x
