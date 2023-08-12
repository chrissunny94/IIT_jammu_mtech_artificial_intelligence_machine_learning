#QUESTION 4 

def jt_dens(x,y):
    if y < x:
        return 0
    else:
        return (12/5)* x* (2-x-y)

Plot_3d(x_limits=(0,1), y_limits=(0,1), f=jt_dens, cstride=4, rstride=4)
