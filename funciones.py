import random
import math
#ejercicio funciones

def digit_summary(number):
    summary = 0
    while number > 0:
            if (number < 10):
                digit = number
                summary = summary + digit
                number = int(number / 10)
            else:
                digit = number % 10
                summary= summary + digit
                number = int(number / 10)
    return summary

#ejercicio corregir funciones

def most(a,b):
    if (a>b):
        return a
    else:
        return b

def least(a,b):
    if (a<b):
        return a
    else:
        return b
    
#AHORCADO

#funcion para elegir palabra

def word_choose(hanged_list):
    return hanged_list[random.randint(0,len(hanged_list) - 1)]

#funcion para generar los espacios de la palabra a adivinar

def generate_spaces(choose_word):
    guess = ""
    for i in range(len(choose_word)):
        guess += "_"
    return guess

#Funcion para comprobar si la letra esta en la palabra

def letter_in_word(letter,choose_word):
    if (letter in choose_word):
        return True
    else:
        return False

#Funcion para rellenar los espacios con la letra adivinada

def update_guess_word(letter_guess,choose_word,guess_wordd):
    print("La letra se encuentra en la palabra!")
    word_guess = ""
    for i in range(len(choose_word)):
        if (letter_guess == choose_word[i]):
            word_guess += letter_guess
        else:
            word_guess += guess_wordd[i]
    return word_guess

#Funcion para validar la letra a adivinar ingresada

def validation_letter():
    letter = "aa"
    while len(letter) != 1:
        letter = input("Introduzca la letra a adivinar: ")
        if (len(letter) != 1):
            print("No esta ingresando solo una letra, vuelva a ingresar")
        else:
            pass
    return letter

#TP 5
# ejercicio_1

def dni(dni):
    if len(dni)<=8 and len(dni)>=7:
        return True
    else:
        return False

# ejercicio_2

def last_word_len(phrase):
    words = phrase.split()

    last_word = words[-1]
    last_word_length = len(last_word)
    return last_word_length

#ejercicio_3

#ejercicio_4

def multiplos(a,b):
    if (a%b==0):
        return print(f"{a} es multiplo de {b}")

#ejercicio_5

def temperature(min,max,avg):
    avg = (min + max) / 2
    return avg

#ejercicio_6

def split(a):
    a = " ".join(a)
    return a
#ejercicio_7

#ejercicio_8

def circle(radius):
    p = (2*math.pi) * radius
    a = math.pi * (radius*radius)
    return p,a

#ejercicio_9



#ejercicio_13
def vector_length(vector):
    return len(vector)

#ejercicio_14

def prime_number(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

#ejercicio_15

def factorial(num):
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    return resultado

#ejercicio_16

def appareances(num,num_to_find,c):
    num=str(num)
    
    for i in range(len(num)):
        if (num[i]==num_to_find):
            c = c + 1
    return c
