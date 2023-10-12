#solicitar numeros al usuario hasta que ingrese 0, por cada numero mostrar la suma de sus digitos. al finalizar mostrar la sumatoria de todos y la suma de sus digitos
import funciones
number = 1
summary = 0
while number != 0:
    number = int(input("Ingrese un numero: "))
    print(funciones.digit_summary(number))
    summary = summary + number
print(f"la suma de todos los numeros es {summary}")
print(f"la suma de los digitos del total es: {funciones.digit_summary(summary)}")
#print(summary)
#print(total_digit summary)

