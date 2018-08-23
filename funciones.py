#cree una funcion que sume matrices de nxn
m1=[[1,1],[2,2]]
m2=[[3,3],[4,4]]
m3=[[0,0],[0,0]]
def sumatriz():
    for x in range(2):
        for m in range(2):
            m3[x][m]=m1[x][m]+m2[x][m]
    print m3
#crear funcion que retorne el producto punto
def MultMatrix():
    for k in range(dim[0]):
        for x in range(dim2[1]):
            l=0
            for j in range(dim[1]):
                l+= m1[k][j] * m2[j][x]
                m3[k][x] = l
    print m3
