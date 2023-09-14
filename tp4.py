#1. Create a while loop with the following characteristics:

#• The initial value of the variable x will be 0.
#• The increment value will be 1.
#• The exit condition of the loop will be greater than or equal to 30.
#• The execution must be broken when x is equal to 15.
#• You must print the following sentence each time the loop executes: 'The value of the loop is: ' + x.
#• You must skip the executions with the value of x in 4, 6 and 10.
#• At each execution jump, you must display the jumped values with this message: 'The value ' + x ' of x was skipped'.
#• When the execution of the loop is broken, you must show a message indicating it: 'The execution of the loop was broken when x was ' + x.
#• The console output should look like this: 

x = 0
while x < 30:
    x= x + 1
    if x != 4 and x != 6 and x != 10:
        print("The value of the loop is: ",x)
        if x == 15:
            break
    else:

        print(f"The value {x} of x was skipped")

print(f"The execution of the loop was broken when x was {x}")

#1.	Escriba un programa que acepte una secuencia de líneas e imprima todas las líneas convertidas en mayúsculas. Deje una línea en blanco para indicar que ha finalizado la entrada de líneas.

lines = []
while True:
    line = input("Ingrese una linea para convertirla a mayuscula o una linea vacia para finalizar: ")
    if (line != ""):
        lines.append(line)
    else:
        break
for i in range(len(lines)):
    print(f"linea {i + 1} en mayusculas: {lines[i].upper()}")

#2.	Escriba un programa que administre una cuenta bancaria, usando una bitácora de operaciones.
#La bitácora de operaciones tiene la siguiente forma:
#D 100
#R 50

#D 100 significa que depositó 100 pesos
#R 50 significa que retiró 50 pesos

#Ejemplo de una entrada:
#D 200
#D 200
#R 100
#D 50
#Introducir una línea vacía indica que ha finalizado la bitácora.
#La salida de éste programa sería:
#350

money_in_account = 0

while True:
    deposit_withdrawal = input("Ingrese D $ para depositar, R $ para retirar y línea vacía para finalizar: ").upper()

    if deposit_withdrawal == "":
        print("Bitácora de operaciones finalizada")
        break
    elif deposit_withdrawal[0] == "R":
        if money_in_account == 0:
            print("No puede retirar, no tiene fondos en su cuenta")
        else:
            money_in_account -= int(deposit_withdrawal[2:])
    elif deposit_withdrawal[0] == "D":
        money_in_account += int(deposit_withdrawal[2:])
    else:
        print("Entrada no válida")

print(f"Dinero total en su cuenta bancaria: ${money_in_account}")

#3.	Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero.
#Imprimir la cantidad total de números primos ingresados.
#Nota: Un número primo es un número natural mayor que 1 que tiene únicamente dos divisores distintos: él mismo y el 1.

n=1
prime_numbers = 0

while n!=0:
    n= int(input("Ingrese un numero: "))
    if n%2!=0:
        prime_numbers = prime_numbers + 1
    else:
        continue
print(f"Usted ingreso {prime_numbers} numeros primos")

#4.	Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, que sean bisiestos y múltiplos de 10.
#Nota: Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.

a = int(input("Ingrese el primer año: "))
b = int(input("Ingrese el segundo año: "))
for i in range(a, b+1):
    if (i % 10 != 0):
        continue
    elif (i % 4 != 0):
        continue
    elif (i % 100 != 0 or i % 400 == 0):
        print(f"El año {i} es bisiesto y multiplo de 10")
    else:
        pass


#5.	Escribe un programa que imprima todos los números pares del 1 al 20 usando un bucle for. Utiliza la declaración continue para omitir los números impares.

for i in range(1,20+1):
    if i%2 != 0:
        continue
    print("numero: ", i)

#6.	Crea una lista de números y utiliza un bucle for para encontrar un número específico. Cuando encuentres el número, usa break para salir del bucle.

number_list = 80
n= int(input("Ingrese el numero que quiere buscar: "))
for i in range(n+1):
    print(i)
    if i==n:
        break
print("Este es el numero que buscaba")

#7.	Crea un programa que muestre un menú de opciones (por ejemplo, opciones 1, 2, 3). Utiliza un bucle while para permitir al usuario seleccionar una opción. Si el usuario ingresa "0", utiliza break para salir del bucle (Mostrar un mensaje por cada opción elegida).

op = 1

while op != 0:
    op= int(input("Ingrese una opcion ( 1 || 2 || 3):  "))
    if op == 1:
        print("Esta es la opcion 1")
    elif op == 2:
        print("Esta es la opcion 2")
    elif op == 3:
        print("Esta es la opcion 3")
    elif op == 0:
        break
    else:
        print("Ingrese una opcion valida (1,2,3)")
print("Usted salio del bucle")