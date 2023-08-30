
#Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene. Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.

n = int(input("Ingrese un numero para saber si sus digitos son pares o impares: "))
pares = 0
impares= 0
while n > 0:
    n = n // 10
    if n % 2 == 0:
        pares = pares + 1
    else: 
        impares = impares + 1


print(f"el numero tiene {pares} digitos pares y {impares} digitos impares")