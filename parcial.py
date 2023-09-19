#Pedir al usuario su nombre. Cada vez que el programa interactúe con él debe llamarlo por su nombre.
#    Generar un menú de opciones, que serán:
#       Juego de números.
#       Juego de palabras.
#Si el usuario elige la primera opción, se debe pedir el ingreso de números enteros (condición de salida: cuando ingrese 0). Al finalizar mostrar por pantalla:
#   El mayor número par.
#   El promedio de los números impares.
#   Si el usuario elige la segunda opción, se debe pedir el ingreso de una frase y mostrar por pantalla la cantidad de cada vocal que contiene dicha frase.

operation = 1
    #pedimos al usuario su nombre
name = input("Ingrese su nombre: ").title()

while operation == 1:

    #abrimos el menu de opciones de juegos y declaramos las variables a utilizar en el juego
    option = int(input(f"BIENVENIDO {name}: Juego de numeros (1) || Juego de palabras (2)    "))
    #par mas alto
    largest_pair = 0
    #numeros impares total
    odd_numbers = 0
    #contador de numeros impares
    odd_counter = 0

    #JUEGO DE NUMEROS
    
    if option == 1:
        print("| JUEGO DE NUMEROS |")
        number = 1
        while number != 0:
            number = int(input(f"{name} tenes que ingresar numeros enteros, cuando termines, ingresa 0:   "))
            if number % 2==0:
                if number > largest_pair:
                    largest_pair = number
            elif number == 0:
                break
            else:
                odd_counter = odd_counter + 1
                odd_numbers = odd_numbers + number
                odd_numbers_average = odd_numbers / odd_counter
        print(name,", el numero par mas grande que ingresaste fue el ",largest_pair,", y el promedio de los impares es: ",odd_numbers_average)
        operation = int(input(f"{name}, si queres jugar otro juego apreta (1), si queres salir apreta (2)  "))
    
    #JUEGO DE PALABRAS
    
    if option == 2:
        phrase = input(f"{name} ingresa una frase para saber que vocales contiene: ").lower()
        #inicializamos los contadores de cada vocal
        a = 0
        e = 0
        i = 0
        o = 0
        u = 0
        #ponemos un bucle for para recorrer la palabra y comparamos con las vocales para poder sumarlas a su contador respectivo
        for j in range(len(phrase)):
            if phrase[j] == "a":
                a = a + 1 
            elif phrase[j] == "e":
                e = e + 1
            elif phrase[j] == "i":
                i = i + 1
            elif phrase[j] == "o":
                o = o + 1
            elif phrase[j] == "u":
                u = u + 1
        #imprimimos la cantidad de vocales que contenia la frase
        print(f"{name}, en la frase habian {a} letras a, {e} letras e, {i} letras i, {o} letras o y {u} letras u")
        operation = int(input(f"{name}, si queres jugar otro juego apreta (1), si queres salir apreta (2)  "))

print(f"Gracias por jugar, hasta pronto {name}!")
