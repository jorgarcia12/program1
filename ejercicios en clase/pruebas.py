import funciones
numbers_list = [45, 120, 49, 38, 12, 10, 5]

print(f"La lista original es:  {numbers_list}")
n = int(input("Ingrese un numero para buscarlo en la lista: "))
result = funciones.busqueda_binaria(numbers_list,n)

if result != -1:
    print(f"El numero {n} se encuenttra en la posicion {result}")
else:
    print(f"El numero {n} no se encontro en la lista")