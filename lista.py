list = [1, 2, 3, 4, 5]
list.append(9)
print list

list = []
list.append(8)
list.append(12)
list.append(2)
list.append(0)
list.append(4)
print list

lista1 = ['alba', 1, 2, 3]
lista2 = ['listas', 'hola', 5, 8]
lista3 = lista1 + lista2
print lista3

import random
def intersectarLista(lista, lista4):
lista = [2, 4, 6, 8]
lista4 = [4, 6, 9, 10]
lista_nueva=[]
    for a in lista:
        for b in lista4:
            if a == b:
                if a not in lista_nueva:
                    lista_nueva.append(a)

                    return lista_nueva
