def convert(nubmer):
    valor = False
    cadena = ''
    a = "Pling"
    b = "Plang"
    c = "Plong"
    if nubmer % 3 == 0:
        cadena = a
        valor = True
    if nubmer % 5 == 0:
        cadena = cadena + b
        valor = True
    if nubmer % 7 == 0:
        cadena = cadena + c
        valor = True
    if valor == False:
        return str(nubmer)
    else:
        return cadena