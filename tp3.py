#1-	Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

word = input("Ingrese una palabra: ")
for i in range(10):
    print(word)

#2-	Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

age = int(input("Ingrese su edad: "))
for i in range(1, age+1):
    print(i)

#3-	Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.


n = int(input("ingrese un numero positivo para ver los impares hasta ese numero: "))
for i in range(n+1):
    if i % 2 != 0:
        print(i, end = ", ")

#4-	Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

n = int(input("Ingrese un numero para hacer cuenta atras: "))
for i in range(-1,n):
    print(n, end = ", ")
    n=n-1

#5-	Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

capital_investment = int(input("Ingrese el capital a invertir: "))
annual_interest = float(input("Ingrese el interes anual: "))
years = int(input("Ingrese cuantos años quiere realizar la inversion: "))
annual_interest = annual_interest / 100 
for i in range(years):
    investment = capital_investment*annual_interest
    capital_investment= capital_investment + investment
    print(f"Usted genero: ${investment}")
    total_investment = investment + investment
print(f"Usted saco un total de ${total_investment}")

#6-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

height = int(input("Ingrese la altura del triangulo en numero: "))
for i in range(height+1):
    print("*" * i)

#7-	Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.

for n in range(1, 10+1):
    print(f"Tabla de multiplicar del {n}:")
    for i in range(1, 10+1):
        result = n * i
        print(f"{n} x {i} = {result}")
    print("----------") 

#8-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

height = int(input("Ingrese la altura del triangulo en numero: "))
for i in range(1, height + 1, 2):
    for j in range(i, 0,-2):
            print(j ,end= " ")
    print()

#9-	Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

password= str
while password != "1234":
    password = input("Ingrese la contraseña (pista: 1234)")
    if password != "1234":
        print("Contraseña erronea")
if password == "1234":
    print("contraseña correcta, bienvenido")

#10-	Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

n = int(input("Ingrese un numero para saber si es primo o no: "))
if n <= 1:
    es_primo = False
else:
    es_primo = True
for i in range(2,n):
    if n % i == 0:
        es_primo = False
    break
if es_primo == True:
    print("es primo")
else:
    print("no es primo")

#11-	Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

word = input("Ingrese una palabra para verla dada vuelta: ")
upside_down = word[::-1]
print(upside_down)

#12-	Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

phrase = input("ingrese una frase: ").lower()
letter = input("ingrese una letra para ver cuantas veces aparece en la frase: ").lower()
count = 0

for i in range(len(phrase)):
    if letter == phrase[i]:
        count = count + 1
print(f"la letra {letter} aparece {count} en la frase")

#13-	Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

while True:
    echo = input("Introduzca algo o salir si quiere hacerlo: ")
    if (echo.lower() == "salir"):
        break
    print(echo)


#14-	Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo.

first = int(input("Introduzca el primer numero: "))
second = int(input("Introduzca el segundo numero: "))
for i in range(first,second + 1):
    if (i % 2 == 0):
        print(f"{i} es par")
    else:
        print(f"{i} es impar")

#15-	Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.

number = int(input("Ingrese un numero entero mayor a cero para saber sus divisores: "))

for i in range(1,number+1):
    if number % i == 0:
        print(f"{i} es divisor de {number}")

#16-	Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.

how_many = int(input("Ingrese cuantos numeros va a ingresar: "))
count= 0
for i in range(how_many):
    number = int(input("Ingrese un numero: "))
    if number < 0:
        count = count + 1
print(f"Usted ingreso {count} numeros negativos")


#17-	Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas).

phrase = input("Ingrese una frase para saber que vocales contiene: ")
a = 0
e = 0
i = 0
o = 0
u = 0
for j in range(len(phrase)):
    if phrase[j] == "a":
        a = a + 1 
    elif phrase[j] == "e":
        e= e + 1
    elif phrase[j] == "i":
        i= i + 1
    elif phrase[j] == "o":
        o= o + 1
    elif phrase[j] == "u":
        u= u + 1

print(f"en la frase habian {a} letras a, {e} letras e, {i} letras i, {o} letras o y {u} letras u")

#18-	Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…

n = 10
a, b = 0 , 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#19-	Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. El programa deberá comprobar que las cantidades ingresadas sean positivas.

goal = int(input("Ingrese la cantidad que quiere ahorrar: "))
savings = 0
while savings < goal:
    money = int(input("Ingrese el dinero que va a meter en la alcancia: "))
    savings = savings + money
print(f"Usted llego a la meta de ${goal} con ${savings}")

#20-	Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.
n=1
summatory = 0
while n!=0:
    n=int(input("Ingrese un numero entero: "))
    summatory = summatory + n
print(f"La sumatoria de todos los numeros es {summatory}")

#21-	Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.

n=1
highest = 1
iterator = 0
while n != 0:
    n=int(input("Ingrese un numero: "))
    iterator = iterator + 1
    if (n == 0):
        break
    elif (iterator == 1):
        highest = n
    elif (n>highest):
        highest=n
print(f"el mayor numero ingresado fue el {highest}")

#22-	Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.

even = 0
while True:
    addition = 0
    number = int(input("Ingrese enteros positivos o -1 para finalizar: "))
    if (number % 2 == 0):
        even = even + 1
    else:
        pass
    if (number == -1):
        print("Finalizando...")
        break
    else:
        while number > 0:
            if (number < 10):
                digit = number
                addition += digit
                number = int(number / 10)
            else:
                digit = number % 10
                addition += digit
                number = int(number / 10)
        print(f"La suma de los digitos del numero {number} es {addition}")
print(f"Ingreso {even} numeros pares")


#23-	Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0.

payment = 0
total_amount = 0
while True:
    payment= payment + 1
    amount = float(input(f"Ingrese el monto de la compra {payment}, ingrese 0 para finalizar: "))
    if (amount == 0):
        print("Finalizando...")
        break
    else:
        total_amount = total_amount + amount
print(f"El monto total de la compra fue de ${total_amount}")

#24-	Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.

payment = 0
total_amount = 0
while True:
    payment= payment + 1
    amount = float(input(f"Ingrese el monto de la compra {payment}, ingrese 0 para finalizar: "))
    if (amount == 0):
        print("Finalizando...")
        break
    elif (amount < 0):
        print("No puede ingresar montos negativos")
    else:
        total_amount += amount
if (total_amount > 1000):
    print("Por superar el monto de $1000 se la aplicara un 10% de descuento")
    total_amount = total_amount * 0.90
    print(f"Monto total a pagar: ${total_amount}")
else:
    print(f"El monto total de la compra fue de ${total_amount}")

#25-	Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número. El factorial de 0 es 1.

n = int(input("Ingrese un entero positivo para ver su factorial: "))
fact = 1
if (n == 0):
    print("0! = 1")
else:
    for i in range(n,0,-1):
        fact = fact * i
    print(f"{n}! = {fact}")