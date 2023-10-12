import funciones_tp5

counter = 0
eldest_number = 0
while True:
    number = int(input("Ingrese un numero primo o uno no primo para finalizar: "))
    if (funciones_tp5.prime_number(number)):
        if (number > eldest_number):
            eldest_number_number = number
        digit_addition = funciones_tp5.digit_summary(number)
        print(f"La suma de los digitos del numero {number} es {digit_addition}")
        num_to_find = int(input("Ingrese un digito para saber cuantas veces aparece en el numero: "))
        print(f"El numero {num_to_find} aparece {funciones_tp5.appareances(number,num_to_find,counter)} veces en el numero: {number}")
    else:
        break
factorial_eldest_number = funciones_tp5.factorial(eldest_number)
print(f"El mayor numero ingresado primo fue {eldest_number} y su factorial es {factorial_eldest_number}!")