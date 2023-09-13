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

#3.	Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero.
#Imprimir la cantidad total de números primos ingresados.
#Nota: Un número primo es un número natural mayor que 1 que tiene únicamente dos divisores distintos: él mismo y el 1.

#4.	Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, que sean bisiestos y múltiplos de 10.
#Nota: Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.

#5.	Escribe un programa que imprima todos los números pares del 1 al 20 usando un bucle for. Utiliza la declaración continue para omitir los números impares.

#6.	Crea una lista de números y utiliza un bucle for para encontrar un número específico. Cuando encuentres el número, usa break para salir del bucle.

#7.	Crea un programa que muestre un menú de opciones (por ejemplo, opciones 1, 2, 3). Utiliza un bucle while para permitir al usuario seleccionar una opción. Si el usuario ingresa "0", utiliza break para salir del bucle (Mostrar un mensaje por cada opción elegida).
