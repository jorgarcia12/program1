import funciones
#ORDENAMIENTO
#Bubble Sort
numbers_list = [45, 120, 49, 38, 12, 10, 5]
print("BUBBLE SORT:")
print(f"La lista original es:  {numbers_list}")
print("------------------------------------------------------------")
funciones.bubble_sort(numbers_list)
print(f"La lista ordenada es: {numbers_list}")

#Selection Sort
numbers_list = [45, 120, 49, 38, 12, 10, 5]
print("SELECTION SORT: ")
print(f"La lista original es:  {numbers_list}")
print("------------------------------------------------------------")
funciones.selection_sort(numbers_list)
print(f"La lista ordenada es: {numbers_list}")

#Insert Sort
numbers_list = [45, 120, 49, 38, 12, 10, 5]
print("INSERTION SORT:")
print(f"La lista original es:  {numbers_list}")
print("------------------------------------------------------------")
funciones.insertion_sort(numbers_list)
print(f"La lista ordenada es: {numbers_list}")

#Merge Sort
numbers_list = [45, 120, 49, 38, 12, 10, 5]
print("MERGE SORT:")
print(f"La lista original es:  {numbers_list}")
print("------------------------------------------------------------")
funciones.merge_sort(numbers_list)
print(f"La lista ordenada es: {numbers_list}")

#BUSQUEDA
#Busqueda lineal

numbers_list = [45, 120, 49, 38, 12, 10, 5]
print(f"La lista original es:  {numbers_list}")
n = int(input("Ingrese un numero para buscarlo en la lista: "))
result = funciones.lineal_search(numbers_list,n)

if result != -1:
    print(f"El numero {n} se encuenttra en la posicion {result}")
else:
    print(f"El numero {n} no se encontro en la lista")

#Busqueda binaria
funciones.bubble_sort(numbers_list)
print(f"La lista original es:  {numbers_list}")
n = int(input("Ingrese un numero para buscarlo en la lista: "))
result = funciones.binary_search(numbers_list,n)
if result != -1:
    print(f"El numero {n} se encuentra en la posicion {result}")
else:
    print(f"El numero {n} no se encontro en la lista")
