import funciones

"""
Turnero de banco con 3 posibles operaciones.

La funcion pregunta  da bienvenida al usuario y le pregunta la operacion que desea realizar en el banco.
"""
def pregunta():

    print("Bienvenido al Banco del sueño ")

    while True:
        print("[C] - Caja \n[P] - Cliente con Prioridad \n[M] - Moneda extranjera")
        try:
            mi_operacion = input("Elija su operacion: ").upper()
            ["C", "P", "M"].index(mi_operacion)

        except ValueError:
            print("Esa no es una opción válida, vuelva a intentarlo")

        else:
            break

    funciones.decorador(mi_operacion)

"""
la funcion inicio comienza el programa del turnero y pregunta si desea hacer otro tipo de operacion
"""
def inicio():

    while True:
        pregunta()
        try:
            otro_turno = input("Quieres sacar otro tipo de operacion? [S] [N]: ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:

            print("Esa no es una opción válida")
        else:

            if otro_turno == "N":
                print("Gracias por su visita")
                break
if __name__== '__name__'


inicio()


