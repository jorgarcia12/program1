import funciones_tp7


numbers_list = []
while True:
    number = int(input("Ingrese un numero para agregarlo a la lista o ingrese '0' para terminar: " ))
    if number==0:
        break
    else:
        numbers_list.append(number)

print(f"La lista original es: {numbers_list}")
funciones_tp7.bubble_sort_reverse(numbers_list)
print(f"La lista ordenada de mayor a menor es: {numbers_list}")