#! /usr/env/ python

class matriz:
    def __init__(self):
        self.s = []

    def DimMatrix(self,m):
        a = len(m)
        for x in m:
            b = len(x)
        return [a,b]

    def DoMatrix(self):
        print "\n"
        a = int(input("Ingrese el numero de filas "))
        b = int(input("Ingrese el numero de columnas "))
        matrix = []
        for c in range(a):
            matrix.append([2]*b)

        for f in range(0,a):
            for c in range(0,b):
                n = int(input("Ingrese el valor para la posicion {} {} de la matriz ".format(f,c)))
                matrix[f][c] = n
        return matrix

    def SumMatrix(self):
        m = self.DoMatrix()
        n = self.DoMatrix()
        dim = self.DimMatrix(m)
        dim2 = self.DimMatrix(n)
        for x in range(dim[0]):
            self.s.append([1]*dim[1])
        for f in range(dim[0]):
            for c in range(dim[1]):
                self.s[f][c] = m[f][c] + n[f][c]
        return self.s

    def MultMatrix(self):
        m = self.DoMatrix()
        n = self.DoMatrix()
        dim = self.DimMatrix(m)
        dim2 = self.DimMatrix(n)
        if dim[1] == dim2[0]:
            for x in range(dim[0]):
                self.s.append([1]*dim2[1])

            for k in range(dim[0]):
                for x in range(dim2[1]):
                    l=0
                    for j in range(dim[1]):
                        l+= m[k][j] * n[j][x]
                    self.s[k][x] = l
        print self.s
