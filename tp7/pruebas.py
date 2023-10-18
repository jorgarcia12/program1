import funciones_tp7

strings_list = []
while True:
    string = input("Ingrese una palabra para meterla en la lista, o ingrese 'x' para terminar: ")
    if string == 'x':
        break
    else:
        strings_list.append(string)
funciones_tp7.insertion_sort(strings_list)
print(strings_list)
