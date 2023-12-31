import funciones_tp5

#1.	Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.

dni = int(input("Ingrese su numero de DNI: "))
print(funciones_tp5.dni(dni))

#2.	Escribir una función que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras están separadas por uno o más espacios. También podría haber espacios al principio o al final del string pasado por parámetro.

phrase = input("Ingrese una frase para saber la longitud de la ultima palabra: ")
print(funciones_tp5.last_word_len(phrase))

#3.	Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club. Para eso ingresará nombre completo y número de DNI de cada socio, indicando que finalizará el procesamiento mediante el ingreso de un nombre vacio.
#Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse más de un nombre, en cuyo caso será: nombre1, nombre2, apellido. Si un socio tuviera más de un apellido, el usuario solo ingresará uno.
#Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa debe dejar al usuario en un bucle hasta que ingrese un DNI correcto.
#Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre, la cantidad de letras del apellido y los 3 primeros dígitos de su DNI. Ejemplo:
#Nombre: María Ines Rosales
#DNI: 25469648
#ID -> Maria7254

while True:
    dni = input("Introduzca el numero de dni: ")
    while funciones_tp5.dni(dni) == False:
        dni = input("Introduzca el numero de dni: ")
    name = input("Ingrese el nombre completo o teclee enter para finalizar : ")
    if (name == ""):
        break
    id = funciones_tp5.identifier(name, dni)
    print(f"Su identificador es {id}")

#4.	Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. Crea una función que reciba los dos números, y devuelve si el primero es múltiplo del segundo.
n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese un numero: "))
if (funciones_tp5.multiplos(n1,n2)):
    print(f"{n1} es multiplo de {n2}")
else:
    print("Ningun numero es multiplo del otro")


#5.	Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.
avg = 0
days = int(input("Ingrese la cantidad de dias que quiere ingresar: "))
while days !=0:
    min = int(input("Ingrese la temperatura minima del dia: "))
    max = int(input("Ingrese la temperatura maxima del dia: "))
    print(f"la temperatura media es de {funciones_tp5.temperature(min,max,avg)}")
    days= days - 1
print("Se realizo la media de todos los dias ingresados")

#6.	Crea una función que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función.

phrase = input("Ingrese una frase para que la misma se devuelva con un espacio entre las letras: ")
print(funciones_tp5.split(phrase))

#7.	Crea una función que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.

numbers_list = []
for i in range(5):
    number = int(input("Introduzca un numero: "))
    numbers_list.append(number)
max_number, min_number = funciones_tp5.max_min(numbers_list)
print(f"El numero minimo ingresado fue el {min_number}, y el maximo fue el {max_number}")

#8.	Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.

radius = int(input("Ingrese el radio de la circunferencia para conocer su area y perimetro: "))
print(f"El perimetro y area del circulo son: {funciones_tp5.circle(radius)}")

#9.	Crear una subrutina llamada “login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.
#Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.

attempts = 0
while (attempts<=3):
    user = input("Ingrese el usuario: (usuario1)  ")
    password = input("Ingrese la contraseña: (asdasd)  ")
    if (funciones_tp5.login(user,password)==True):
        print("Bienvenido ")
        break
    else:
        print("Datos invalidos, intente nuevamente ")
        attempts = attempts +1
if (attempts >= 3):
    print("Demasiados intentos erroneos, cerrando programa")


#10.	Escribir una función que aplique un descuento a un precio. Esta función tiene que recibir un diccionario con los precios y porcentajes del carrito de compra, aplicar los descuentos a los productos del carrito  y devolver el precio final de la compra.

products_dictionarie = {500:50,4500:48,230:10.3}
i = 0
for key, value in products_dictionarie.items():
    i += 1
    final_prize = funciones_tp5.discount(key,value)
    print(f"Precio producto {i}: ${key}")
    print(f"Descuento producto {i}: %{value}")
    print(f"Precio final del producto {i}: ${final_prize}")


#11.	Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista.

num_listt = [1,2,3,4,5,6]
new_listt = funciones_tp5.list_new(num_listt)
print(new_listt)

#12.	Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.

phrase = input("Ingrese una frase: ")
word_dictionarie = funciones_tp5.lenght_dictionarie(phrase)
print(word_dictionarie)

#13.	Escribir una función que calcule el módulo de un vector.

vector = {"Hola"," Buenas", "Tardes"}
print(funciones_tp5.vector_length(vector))

#14.	Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una función booleana que lo decida.

num = int(input("Ingresa un numero para saber si es primo: "))
if (funciones_tp5.prime_number(num)):
    print(f"El numero {num} es primo")
else:
    print(f"El numero {num} no es primo")

#15.	Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, al finalizar, la cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.
num = 1
counter = 0

while num !=0:
    num = int(input("Ingrese numeros para saber sus factoriales, cuando quiera terminar ingrese 0: "))
    if (num==0):
        break
    counter = counter + 1
    print(funciones_tp5.factorial(num))
print(f"Se mostro el factorial de {counter} numeros")
    

#16.	Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de ocurrencias del dígito en el número, utilizando para ello una función que calcule la frecuencia.

counter = 0
num = (input("Ingrese un numero: "))
num_to_find = (input("Ingrese el numero que quiere buscar en el numero anterior: "))
print(f"El numero {num_to_find} aparece {funciones_tp5.appareances(num,num_to_find,counter)} veces en el numero: {num}")

#17.	Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un número que no sea primo. Por cada número, mostrar la suma de sus dígitos. También solicitar al usuario un dígito e informar la cantidad de veces que aparece en el número (frecuencia). Al finalizar el programa, mostrar el factorial del mayor número ingresado.

counter = 0
eldest_number = 0
while True:
    number = int(input("Ingrese un numero primo o uno no primo para finalizar: "))
    if (funciones_tp5.prime_number(number)):
        if (number > eldest_number):
            eldest_number_number = number
        digit_addition = funciones_tp5.digit_summary(number)
        print(f"La suma de los digitos del numero {number} es {digit_addition}")
        digit = int(input("Ingrese un digito para saber cuantas veces aparece en el numero: "))
        print(f"El numero {num_to_find} aparece {funciones_tp5.appareances(num,num_to_find,counter)} veces en el numero: {num}")
    else:
        break
factorial_eldest_number = funciones_tp5.factorial(eldest_number)
print(f"El mayor numero ingresado primo fue {eldest_number} y su factorial es {factorial_eldest_number}!")
    