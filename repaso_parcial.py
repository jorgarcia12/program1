import random


#El programa pedira que el usuario ingrese una palabra que sea palindromo (que se lea igual de izquierda a derecha y de derecha izquierda) para ingresar al juego. El juego zconsiste en adivinar un numero elegido al azar, y el usuario tendra 5 intentos para adivinarlo


# Con este bucle while, ingresamos al juego 
print("BIENVENIDO AL JUEGO!!")
while True:

    # una vez que ingresamos el programa le pedira al usuario un palabra
    # Si la palabra es palindromo entrara al juego, sino tendra que ingresar otra palabra
    print("------------------------------------------------------------------")
    print("PARA INGRESAR AL JUEGO INGRESE UNA PALABRA QUE SEA PALINDROMO (que se lea igual de izquierda a derecha y de derecha izquierda): ")
    word = input("Ingrese su palabra(Ingrese 0 para salir del juego): ")
    equals_letter = 0
    reverse_word = ""
    guess = False

    # Si el usuario ingreso un 0, se cierra el juego. si el usuario ingreso una palabra entra al condicional
    if (word != "0"):

        # una vez dentro, el programa asignara la misma palabra pero alrevez con un bucle for
        for i in range(len(word)-1,-1,-1):
            reverse_word += word[i]
        
        # con este if comparara la 2 palabra para ver si es palindromo
        if (word == reverse_word):
            # Si entra en esta sentencia significa que entro al juego, ahora tendra 5 intentos para acertar el numero
            print("FELICIDADES!!!")
            print("La palabra es palindromo, PODES JUGAR!!")
            print("Vas a tener 5 intentos para ganar, SINO perdera el juego!!")
            print("")
            random_number = random.randint(0,100)
            attemps = 0
            # En el siguiente bucle, el usuario tendra que adivinar el numero que fue elegido al azar en la variable random_number
            # y tendra 5 intentos para adivinar el numero
            while True:
                # en el siguiente codicional se mostrara mucho mensajes a medida que el usuario va insertando numeros
                # se le mostraran pistas para poder adivinarlo si el numero es mayor o es menor, si adivino el numero se sale del bucle
                # si se terminan los intentos el usuario se saldra del bucle y perdera el juego
                if attemps < 5:
                    user_number = int(input("Ingrese un numero, entre el 0 y el 100: "))
                    attemps += 1
                    if (user_number > random_number):
                        print("EL numero es mayor!")
                        continue
                    elif (user_number < random_number):
                        print("El numero es menor!")
                        continue
                    else:
                        print("")
                        print("FELICIDADES ADIVINASTE EL NUMERO!!!!")
                        break
                else:
                    print("PERDISTE!!, SE AGOTARON TUS INTENTOS!!")
                    break
        else:
            # Si entra en el else, significa que el usuario no ingreso un numero palindromo y tendra que ingresar otra palabra
            print("La palabra ingresada no es palindromo!!!!")
            print("INGRESE OTRA!!")
            continue
        
    else:
        # Si entra en el else significa que el usuario ingreso 0 para salir 
        break
print("¡¡GRACIAS POR JUGAR!!")
    