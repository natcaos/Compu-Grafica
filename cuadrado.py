def calculararea(base, altura, figura):
    if "triangulo" == figura:
        print "el area del triangulo es", at(base, altura)
    if "rectangulo" == figura:
        print "el area del rectangulo es", ar(base, altura)


def ar(base, altura):
    arear = base*altura
    return arear
def at(base, altura):
    areat = base*altura/2
    return areat

def pedirDatos():
    b = input("Dame base")
    a = input("Dame altura")
    f = raw_input("Dame figura")
    calculararea(b, a, f)



pedirDatos()