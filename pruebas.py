import funciones
funciones.prime_number = True
counter = 0
eldest = 0
while (funciones.prime_number==True):
    num = int(input("Ingrese un numero, si este no es primo el programa se cerrara: "))
    if (num>eldest):
        eldest  = num
    if (funciones.prime_number(num)==False):
        break
    print(funciones.digit_summary(num))
    num_to_find = (input("Ingrese el numero que quiere buscar en el numero anterior: "))
    print(f"El numero {num_to_find} aparece {funciones.appareances(num,num_to_find,counter)} veces en el numero: {num}")
print(funciones.factorial(eldest))
    
    