num = 4
contador_pares = 0
contador_impares = 0
contador_total_pares = 0
contador_total_impares = 0
while num != 0:
    num = int(input("Ingrese un entero positivo para seguir ingresando o 0 para finalizar: "))
    while True:
        if (num > 10):
            digito = num % 10
        else:
            digito = num
        if (digito % 2 == 0):
            contador_pares += 1
        else:
            contador_impares += 1
        if (num > 10):
            num = int(num / 10)
        else:
            break
    
    contador_total_pares = contador_total_pares + contador_pares
    contador_total_impares = contador_total_impares + contador_impares
    
    print(f"El numero tiene {contador_pares} digito/s par/es, y {contador_impares} digito/s impar/es")
    contador_pares = 0
    contador_impares = 0

print(f"La cantidad de digito/s par/es leidos en total fue {contador_total_pares} y impar/es {contador_total_impares}")
