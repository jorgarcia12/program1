import random
import funciones_tp6
# 1.	Solicitar al usuario que ingrese números, estos deben guardarse en una lista. Para finalizar el usuario debe ingresar 0, el cual no debe guardarse.
numbers = []

while True:
    n = int(input("Ingrese un numero para guardarlo en una lista, cuando quiera frenar presione 0: "))
    if n==0:
        break
    else:
        numbers.append(n)

print(numbers)

# 2.	A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
list_length = 15

numbers_list = [random.randint(1, 8)for _ in range(list_length)]
print(numbers_list)
n = int(input("Ingrese un numero, si este se encuentra en la lista, se eliminara la primer ocurrencia: "))
if n in numbers_list:
    numbers_list.remove(n)
    print(f"Se elimino la primer aparicion del numero {n} en la lista")
else:
    print(f"El numero {n} no se encontro en la lista")
print("La lista actualizada queda asi: ")
print(numbers_list)

#3.	Imprimir la sumatoria de todos los números de la lista.

summary = 0

for i in range(len(numbers_list)):
    summary = summary + numbers_list[i]
print(f"La suma de todos los elementos de la lista es: {summary}")

#4.	Solicitar al usuario otro número y crear una lista con los elementos de la lista original, que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.

list_length = 5

number = int(input("Ingrese un numero para crear una lista con numeros menores a este: "))
minor_numbers_list = [random.randint(1,number-1) for _ in range(list_length)]

for i in range(len(minor_numbers_list)):
    print(minor_numbers_list[i])

#5.	Generar e imprimir una nueva lista que contenga como elementos a tuplas, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2], la nueva lista contendrá: [(5,3),(16,1),(2,2),(57,1)]

numbers_list = [5, 5, 2, 25, 32, 5, 2, 25, 32, 1]
counter = {}
for elemento in numbers_list:
    if elemento in counter:
        counter[elemento] += 1
    else:
        counter[elemento] = 1
new_tuple_list = [(elemento, counter[elemento]) for elemento in counter]

print(new_tuple_list)

#6.	Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar ‘x’. A continuación, solicitar que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar ‘x’.
#a.	Informar los nombres de todos los alumnos de nivel primario y de los de nivel secundario, sin repeticiones.
#b.	Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
#c.	Informar qué nombres de nivel primario no se repiten en los de nivel secundario.

primary_names = []
secundary_names = []
no_repeat_list = []
repeat_list = []
all_names = []
print("Nombres primaria")
while True:
    names = input("Ingrese nombres de los alumnos del primario, cuando termine ingrese x: ")
    if names== 'x':
        break
    else:
        primary_names.append(names)
print(primary_names)

print("Nombres secundaria")
while True:
    names = input("Ingrese nombres de los alumnos del secundario, cuando termine ingrese x: ")
    if names == 'x':
        break
    else:
        secundary_names.append(names)
print(secundary_names)

print(f"Todos los nombres del colegio son :{funciones_tp6.all_names(primary_names,secundary_names,all_names)}")
print(f"Los nombres que se repiten entre nivel primario y secundario son: {funciones_tp6.repeated_names(primary_names,secundary_names,repeat_list)}")
print(f"Los nombres q no se repiten entre el nivel primario y secundario son: {funciones_tp6.non_repeated_names(primary_names,secundary_names,no_repeat_list)}")


#7.	Escribir un programa que procese strings ingresados por el usuario. La lectura finaliza cuando se hayan procesado 50 strings. Al finalizar, informar la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados. Ejemplo:
#‘r’:5
#‘%’:3
#‘a’:8
#‘9’:1

appareances = {}
string_counter = 0

while string_counter < 50:
    string = input("Ingrese un string o 'x' para terminar: ")
    if string == 'x':
        break
    string_counter += 1
    for i in string:
        if i in appareances:
            appareances[i] += 1
        else:
            appareances[i] = 1
for i, cant in appareances.items():
    print(f"{i} : {cant}")



#8.	Diez equipos de la liga inter-barrial identificados con los números 1, 2, 3, 4, …, 10, participaron en un campeonato de fútbol con modalidad todos contra todos.
#Los goles anotados en cada encuentro se registraron en el siguiente cuadro:
#Escriba un programa que:
#o	Lea el cuadro de goles en un arreglo de dos dimensiones.
#o	Muestre para cada equipo la cantidad de triunfos, empates y derrotas.
#o	Muestre la diferencia entre el total de goles marcados y el total de goles recibidos.
#o	Determine la cantidad de puntos obtenidos por cada equipo.



#9.	Escribir un programa que simule el juego clásico de Memoria (Memotest) utilizando matrices. El juego consiste en un tablero de cartas boca abajo y el objetivo es encontrar todas las parejas de cartas iguales.


#10.	Teniendo una matriz cuadrada de cualquier dimensión, obtener lo siguiente:
#a.	la diagonal principal.
#b.	la diagonal inversa.

matriz= [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

main_diagonal_result = funciones_tp6.main_diagonal(matriz)
reverse_diagonal_result = funciones_tp6.reverse_diagonal(matriz)

print("Diagonal Principal:", main_diagonal_result)
print("Diagonal Inversa:", reverse_diagonal_result)

#11.	Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

symbols = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
symbols_find = input("Ingrese una moneda para conocer su simbolo: ").title()
valor = symbols.get(symbols_find)
if symbols_find is None:
    print(f"La clave '{symbols_find}' no existe en el diccionario.")
else:
    print(f"El valor asociado a la clave '{symbols_find}' es: {valor}")

#12.	Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje ‘<nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>’.
name = input("Ingrese su nombre: ").title()
age = input("Ingrese su edad: ")
address = input("Ingrese su dirección: ")
phone_number = input("Ingrese su número de teléfono: ")

dictionary = {'nombre': name,'edad': age,'direccion': address,'telefono': phone_number}

print(f"{dictionary['nombre']} tiene {dictionary['edad']} años, vive en {dictionary['direccion']} y su número de teléfono es {dictionary['telefono']}.")

#13.	Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.  

fruits_table = {'tomate' : 10,'naranja' : 5, 'manzana' : 7, 'banana' : 8 }
print(fruits_table)
fruit_selection = input("Ingrese que fruta va a llevar: ")
kilos = int(input("Ingrese cuantos kilos va a llevar: "))
if fruit_selection in fruits_table:
    value = fruits_table[fruit_selection]
    total_price = value * kilos

print(f"Usted llevo {kilos} kilos de {fruit_selection}, su total es de ${total_price}")
