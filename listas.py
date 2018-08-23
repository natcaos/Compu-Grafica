#una lista luego agregar elem al final de la lista usando append
lista=[1,2,3,4,5]
lista.append(1)
print lista
#crear lista vacia, agregar 5 elementos
lista1=[]
for x in range(5):
    lista1.append(x)
print lista1
#crear lista vacia y agregar tantos elementos como el usuario desee
lista2=[]
n = int(input("ingrese la cantidad de numeros "))
for x in range(n):
    a = int(input("ingrese el numero "))
    lista2.append(a)
print lista2
#crear una matriz identidad 3x3 y mostrarla en pantalla
lista3=[[1,0,0],[0,1,0],[0,0,1]]
print lista3
#crear una lista y eliminar los elementos no numericos, usar la instruccion
#remove
lista4=[1,2,4,'a',8]
lista4.remove('a')
print lista4
#crear dos listas y luego unirlas
lista5=[1,2,4]
lista6=[9,7,5]
lista7 = lista5 + lista6
print lista7
#crear dos listas y mostrar en pantalla los valores en comun
lista8=[1,2,3,6]
lista9=[2,6,8,7]

for x in range(len(lista8)):
    for m in range(len(lista9)):
        if lista8[x]==lista9[m]:
            print lista8[x]
#crear dos listas y mostrar todos los elem que estén en la primera lista y que
#no estén en la segunda
lista10=[1,2,3,6]
lista11=[2,6,8,7]

for x in range(len(lista10)):
    for m in range(len(lista11)):
        if lista10[x]!=lista11[m]:
            print lista10[x]
#crear dos listas(vectores) de igual tamaño, luego mostrar la suma de vectores
lista12=[1,2,3]
lista13=[4,5,6]
lista14=[0,0,0]

for x in range(len(lista12)):
    lista14[x]=lista12[x]+lista13[x]
print lista14
