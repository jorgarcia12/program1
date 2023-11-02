import funciones_repaso, random
#Crea un juego de Bingo donde el usuario pueda ingresar los números para generar su propio cartón de bingo. A continuación, se detalla cómo se debe implementar el juego:
# 1. Solicita al usuario que ingrese 25 números únicos, uno a la vez, para completar su cartón de bingo. Los números deben estar en el rango de 1 a 75.
# 2. Valida que los números ingresados sean únicos y estén dentro del rango permitido. Si el usuario ingresa un número duplicado o fuera del rango, debe mostrar un mensaje de error y solicitar otro número.
# 3. Después de que el usuario haya completado su cartón, inicia el juego de Bingo.
# 4. Extrae bolas de bingo al azar y verifica si los números extraídos están en el cartón del usuario.
# 5. Continúa extrayendo bolas de bingo hasta que el jugador complete una línea horizontal, vertical o diagonal en su cartón.
# 6. Muestra mensajes informativos al usuario a medida que se extraen bolas y cuando gana.
# 7. Pregunta al usuario si desea jugar de nuevo al finalizar el juego.

#Recuerda proporcionar instrucciones claras y manejar las entradas del usuario de manera amigable. El objetivo es crear un juego interactivo que permita al usuario disfrutar del Bingo personalizado.
bingo_nums = []
num_count = 0
full_card = False

bingo_nums = funciones_repaso.create_card(bingo_nums,num_count)
print(f"Su CARTON ES EL SIGUIENTE: ")
print(bingo_nums)
print("------------------------------------------")
print("Bienvenido al juego:")

while full_card == False:
    bingo_all_numbers = []
    ball_number = random.randint(1,75)
    bingo_all_numbers.append(ball_number)
    print(f"El numero de la bolilla es el {ball_number}")
    funciones_repaso.check_card(bingo_nums,bingo_all_numbers)