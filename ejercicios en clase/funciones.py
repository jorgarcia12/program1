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

# EJERCICIO 2 - VARIABLES DIMENSIONADAS

def home(buy_list):
    home_list = []
    for i in buy_list:
        if (i[3] not in home_list):
            home_list.append(i[3])
        else:
            pass
    return home_list

#Bubble Sort

def bubble_sort(num_list):
    n = len(num_list)
    for i in range(n):
        intercambio = False
        for j in range(0, n-i-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
                intercambio = True
        if not intercambio:
            break

#Selection Sort

def selection_sort(num_list):
    n = len(num_list)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if num_list[j] < num_list[min_index]:
                min_index = j
        num_list[i], num_list[min_index] = num_list[min_index], num_list[i]

#Insert Sort

def insertion_sort(num_list):
    for i in range(1, len(num_list)):
        key = num_list[i]  
        j = i - 1  
        while j >= 0 and key < num_list[j]:
            num_list[j + 1] = num_list[j]
            j -= 1
        num_list[j + 1] = key

#Merge Sort

def merge_sort(num_list):
    if len(num_list) > 1:
        mid = len(num_list) // 2
        left_half = num_list[:mid]
        right_half = num_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                num_list[k] = left_half[i]
                i += 1
            else:
                num_list[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            num_list[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            num_list[k] = right_half[j]
            j += 1
            k += 1

#Busqueda lineal

def lineal_search(num_list, n):
    for i in range(len(num_list)):
        if num_list[i] == n:
            return i  # Se encontró el valor en la posición i
    return -1 

#Busqueda Binaria

def binary_search(num_list, n):
    left, right = 0, len(num_list) - 1

    while left <= right:
        mid = (left + right) // 2

        if num_list[mid] == n:
            return mid  
        elif num_list[mid] < n:
            left = mid + 1 
        else:
            right = mid - 1  

    return -1 


