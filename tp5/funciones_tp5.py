import math
import random
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
def identifier(name, dni):
    identifier = ""
    last_name = ""
    words = name.split()
    for i in name:
        if (i == " "):
            break
        else:
            identifier += i
    identifier += str(len(words[-1]))
    for i in range(3):
        identifier += dni[i]
    return identifier

#ejercicio_4

def multiplos(a,b):
    if (a%b==0):
        return True
    else:
        False

#ejercicio_5

def temperature(min,max,avg):
    avg = (min + max) / 2
    return avg

#ejercicio_6

def split(a):
    a = " ".join(a)
    return a
#ejercicio_7

def max_min(number_list):
    max_number = number_list[0]
    min_number = number_list[0]
    for i in number_list:
        if (i > max_number):
            max_number = i
        else:
            pass
        if (i < min_number):
            min_number = i
        else:
            pass
    return max_number, min_number

#ejercicio_8

def circle(radius):
    p = (2*3.14) * radius
    a = 3.14 * (radius*radius)
    return p,a

#ejercicio_9

def login(u,p):
    if (u == "usuario1" and p == "asdasd"):
        return True
    else:
        return False

#ejercicio_10
def discount(prize, discountt):
    final_prize = prize * (1 - discountt / 100)
    return final_prize

#ejercicio_11

def modified_list(listt):
    for i in range(len(listt)):
        listt[i] += 1

def list_new(listtt):
    modified_list(listtt)
    return listtt


#ejercicio_12
def lenght_dictionarie(phrase):
    phrase = phrase.split()
    words_dictionarie = {}
    for i in phrase:
        words_dictionarie[i] = len(i)

    return words_dictionarie


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

#ejercicio_17

def digit_summary(number):
    number = str(number)
    addition = 0
    for i in number:
        addition = addition + int(i)
    return addition