#ecuaciones de traslacion
#x' = x + tx
#y' = y + ty
#t=[tx,ty]
#p=[x,y]

def Tras(t,p):
    xp=t[0]+p[0]
    yp=t[1]+p[1]
    pp=[xp,yp]
    return pp

    t=[-20,-10]
    p=[-20,-15]
    print Tras(t,p)
