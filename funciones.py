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
    
        