import funciones_tp7

#1.	Escribe un programa que tome una lista de números como entrada y la ordene en orden ascendente utilizando el método de ordenamiento de burbuja.

numbers_list = []
while True:
    number = int(input("Ingrese un numero para agregarlo a la lista o ingrese '0' para terminar: " ))
    if number==0:
        break
    else:
        numbers_list.append(number)
funciones_tp7.bubble_sort(numbers_list)
print(numbers_list)

#2.	Crea un programa que tome una lista de palabras como entrada y las ordene alfabéticamente en orden ascendente utilizando el método de ordenamiento de selección.

words_list = []
while True:
    word = input("Ingrese palabras para ordenarlas alfabeticamente, para terminar ingrese 'x' : ")
    if word == 'x':
        break
    else:
        words_list.append(word)
funciones_tp7.selection_sort(words_list)
print(words_list)

#3.	Crea una lista de diccionarios, donde cada diccionario contiene información sobre un libro (título, autor, año de publicación, etc.). Luego, escribe un programa que ordene la lista de libros en función de un campo específico, como el año de publicación o el autor.

book_list = [
    {"titulo": "El Gran Gatsby","autor": "F. Scott Fitzgerald", "publicacion": 1925},
    {"titulo": "Matar un ruiseñor", "autor": "Harper Lee", "publicacion": 1960},
    {"titulo": "1984", "autor": "George Orwell", "publicacion": 1949},
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "publicacion": 1967},
    {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "publicacion": 1605},
]

lista_de_libros_ordenada_por_año = sorted(book_list, key=funciones_tp7.book_sort)
print("Lista ordenada segun su año de publicacion")
for libro in lista_de_libros_ordenada_por_año:
    print(f'Título: {libro["titulo"]}, Autor: {libro["autor"]}, Año de Publicación: {libro["publicacion"]}')

#4.	Escribe un programa que tome una lista de cadenas como entrada y las ordene en orden ascendente según su longitud. Puedes utilizar el método de ordenamiento de inserción.

strings_list = []
while True:
    string = input("Ingrese una palabra para meterla en la lista, o ingrese 'x' para terminar: ")
    if string == 'x':
        break
    else:
        strings_list.append(string)
funciones_tp7.insertion_sort(strings_list)
print(strings_list)

#5.	Modifica uno de los ejercicios anteriores para ordenar la lista de números en orden descendente en lugar de ascendente.

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

#6.	Escribe un programa que tome una lista de números enteros y ordene la lista utilizando el algoritmo de ordenamiento por conteo.

numbers_list = [45, 120, 49, 38, 12, 10, 5]
print(f"Lista original: {numbers_list}")
print(f"Lista ordenada: {funciones_tp7.counting_sort(numbers_list)}")

#7.	Crea una lista que contenga tanto números como cadenas de caracteres. Escribe un programa que ordene esta lista de manera que primero estén los números ordenados de menor a mayor y luego las cadenas de caracteres ordenadas alfabéticamente.

mixed_list = [45, "buenas", 120,"hola", 49,"diariamente", 38, "autos", 12, 10, 5]
words = [x for x in mixed_list if isinstance(x,(str))]
numbers = [x for x in mixed_list if isinstance(x,(int,float))]
funciones_tp7.bubble_sort(numbers)
funciones_tp7.bubble_sort(words)
sorted_mixed_list = numbers + words
print(f"Lista original: {mixed_list}")
print(f"Lista ordenada: {sorted_mixed_list}")


#8.	Implementa el algoritmo de ordenamiento Merge Sort y úsalo para ordenar una lista de números.

numbers_list = [45, 120, 49, 38, 12, 10, 5]

print(f"La lista original es: {numbers_list}")
funciones_tp7.merge_sort(numbers_list)
print(f"La lista ordenada de menor a mayor es: {numbers_list}")