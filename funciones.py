def numeros_caja():

    for n in range(1, 1000):
        yield f"C - {n}"


def numeros_prioridad():

    for n in range(1, 1000):
        yield f"P - {n}"


def numeros_monedaextr():

    for n in range(1, 1000):
        yield f"M - {n}"


c = numeros_caja()
p = numeros_prioridad()
m = numeros_monedaextr()

 


def decorador(operacion):
#Decorador del numero/turno que imprime el ticket. 

 

    print("\n" + "*" * 23)
    print("\n" + "Su número es:")
    if operacion == "C":
        print(next(c))
    elif operacion == "P":
        print(next(p))
    else:
        print(next(m))
    print("\n" + "Aguarde y será atendido")
    print("\n" + "Su turno se anunciara por la pantalla" + "\n")
    print("\n" + "*" * 23)
    
