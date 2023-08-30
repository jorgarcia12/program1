#Un grupo de amigos decide organizar un juego de estrategia, para lo cual forman dos equipos de 6 integrantes cada uno, donde un integrante de cada equipo es el “jefe” y los otros 5 son sus “oficiales”.La regla más importante del juego es que sólo se comunicarán mediante un canal común, por lo quedeben buscar la forma de ocultar el contenido de sus mensajes. Uno de los equipos decide utilizar un método antiguo de encriptación llamado “la cifra del césar”, que consiste en correr cada letra del mensaje –considerando la posición de cada una en el alfabeto– una determinada cantidad de lugares. Ejemplo: si el corrimiento es de 2 lugares, la palabra “ATAQUE” se transforma en “CVCSWG”.

#Cada día, el “jefe” del equipo debe enviar un mensaje a cada uno de sus oficiales. Escribir un programa que permita encriptar los 5 mensajes. El corrimiento (cantidad de lugares que se correrán las letras) será dado por el usuario antes de comenzar a encriptar. Los 5 mensajes usarán el mismo corrimiento. 
#Nota: si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se vuelve a comenzar desde la letra “a”. Ejemplo: la palabra “EXTRA” corrida 3 lugares se convierte en “HAWUD”. Utilizando el alfabeto español, de 27 letras, el siguiente cálculo matemático permite volver a comenzar por el principio una vez que se llegó a la “z”: (índice de la letra a correr+corrimiento)%27
#Sólo se encriptarán las letras de los mensajes, dejando al resto de caracteres sin modificación.
print("USTED ES EL JEFE!")
mensaje1 = input("Ingrese el mensaje para el oficial 1: ").lower()
mensaje2 = input("Ingrese el mensaje para el oficial 2: ").lower()
mensaje3 = input("Ingrese el mensaje para el oficial 3: ").lower()
mensaje4 = input("Ingrese el mensaje para el oficial 4: ").lower()
mensaje5 = input("Ingrese el mensaje para el oficial 5: ").lower()
corrimiento = int(input("Indique el corrimiento: "))
abecedario = ("abcdefghijklmnñopqrstuvwxyz")
m1 = ""
m2 = ""
m3 = ""
m4 = ""
m5 = ""
for i in range(len(mensaje1)):
    if mensaje1[i] in abecedario:
        for j in range(len(abecedario)):
            if mensaje1[i] == abecedario[j]:
                m1= m1 + abecedario[(j+corrimiento) % 27]
            else:
                pass
    else:
        m1 = m1 + mensaje1[i]
print("el nuevo mensaje es", m1)

for i in range(len(mensaje2)):
    if mensaje2[i] in abecedario:
        for j in range(len(abecedario)):
            if mensaje2[i] == abecedario[j]:
                m2= m2 + abecedario[(j+corrimiento) % 27]
            else:
                pass
    else:
        m2 = m2 + mensaje2[i]
print("el nuevo mensaje es", m2)

for i in range(len(mensaje3)):
    if mensaje3[i] in abecedario:
        for j in range(len(abecedario)):
            if mensaje3[i] == abecedario[j]:
                m3 = m3 + abecedario[(j+corrimiento) % 27]
            else:
                pass
    else:
        m3 = m3 + mensaje3[i]
print("el nuevo mensaje es", m3)

for i in range(len(mensaje4)):
    if mensaje4[i] in abecedario:
        for j in range(len(abecedario)):
            if mensaje4[i] == abecedario[j]:
                m4 = m4  + abecedario[(j+corrimiento) % 27]
            else:
                pass
    else:
        m4 = m4 + mensaje4[i]
print("el nuevo mensaje es", m4)

for i in range(len(mensaje5)):
    if mensaje5[i] in abecedario:
        for j in range(len(abecedario)):
            if mensaje5[i] == abecedario[j]:
                m5= m5 + abecedario[(j+corrimiento) % 27]
            else:
                pass
    else:
        m5 = m5 + mensaje5[i]
print("el nuevo mensaje es", m5)

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