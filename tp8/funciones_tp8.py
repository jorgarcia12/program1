#ejercicio_1

def digit_counter(n,):
    if n<10:
        return 1
    else:
        return 1 + digit_counter(n//10)
    
#ejercicio_2

def is_pow(n,b):
    if n == b:
        return True
    elif n<b:
        return False
    else:
        return is_pow(n/b,b)
    
#ejercicio_3
def string_in_string(a,b):
    if len(b) < len(a):
        return 0
    elif a[:len(b)] == b:
        return 1 + string_in_string(b,a[len(b):])
    else:
        return string_in_string(b, a[1:])

#ejercicio_4
def pair(n):
    if n == 0:
        return True  
    else:
        return odd(n - 1)

def odd(n):
    if n == 0:
        return False  
    else:
        return pair(n - 1)
    
#ejercicio_5
def highest_in_list(number_list,highest):
    highest = 0
    for i in range(len(number_list)):
        if number_list[i]< highest:
            return highest
        elif number_list[i]>highest:
            highest = highest_in_list(number_list,highest)

#ejercicio_6
def replicate(num_list, n):
    if n == 1:
        return num_list
    else:
        return num_list + replicate(num_list, n - 1)

#ejercicio_7
def summary(n, p):
    if n == 1:
        return p
    else:
        return n * p + summary(n - 1, p)
    
#ejercicio_8
def pascal(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)
    
#ejercicio_9
def combinations(c_list, k, actual="", result=[]):
    if k == 0:
        result.append(actual)
        return

    for caracter in c_list:
        combinations(c_list, k - 1, actual + caracter, result)

#ejercicio_10

def sheet_measure(sheet_n):
    if sheet_n == 0:
        return (841, 1189)  # Hoja A0
    else:
        previous_width, previous_length = sheet_measure(sheet_n - 1)
        new_width = previous_length
        new_length = previous_width / 2
        return (new_width, new_length)
