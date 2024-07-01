#Progemama que relaiza las operaciones de suma, resta, multiplicacion y division,
# a partir del ingreso de 2 valores por parte del usuario.
# MENU DE OPERACIONES MATEMATICAS
respuesta_operacion = 0
respuesta_operacion = float
# defineindo la clase
class Operaciones:
    Valor1 = 0
    Valor2 = 0
    print("==============================================================")
    Valor1 = int(input("Ingrese primer valor para operacion aritmetica "))
    Valor2 = int(input("Ingrese segundo valor para operacion aritmetica "))
# menu de opciones en pantalla.
print("=========================================")
print("**** QUE OPERACION DESEA REALIZAR??? ****")
print("=========================================")
print("<1> SUMA")
print("<2> RESTA")
print("<3> MULTIPLICACION")
print("<4> DIVISION")
print("==========================================")
while True:
    opcion_aritmetica = int(input("ESCOJA OPERACION A REALZAR "))
    print("==========================================")
    if (opcion_aritmetica >= 1  and opcion_aritmetica <=4):
        break
    else:
        print("error, escoja una opcion valida")

calcular = Operaciones()
match opcion_aritmetica:
    case 1:
        respuesta_operacion = calcular.Valor1 + calcular.Valor2
    case 2:
        respuesta_operacion = calcular.Valor1 - calcular.Valor2
    case 3:
        respuesta_operacion = calcular.Valor1  * calcular.Valor2
    case 4:
        respuesta_operacion = calcular.Valor1 / calcular.Valor2
print(respuesta_operacion)




