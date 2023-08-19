#1.	Calcular el perímetro y área de un rectángulo dada su base y su altura.

base=float(input("ingrese base: "))
altura=float(input("ingrese altura: "))
perimetro = base*2 + altura*2
area = base * altura
print("el perimetro es ",perimetro)
print("el area es ", area)

#2.	Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

cateto1 = float(input("ingrese el primer cateto: "))
cateto2 = float(input("ingrese el segundo cateto: "))
hip = (cateto1**2+cateto2**2)*(1/2)
print("la hipotenusa es de ",hip)

#3.	Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

a = float(input("ingrese el primer numero: "))
b = float(input("ingrese el segundo numero: "))

print ("suma: ",a+b)
print ("resta: ",a-b)
print ("division: ",a/b)
print ( "multiplicacion: ",a*b)

#4.	Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es:

f = float(input("ingrese la temperatura en farenheit: "))
c = (f-32)*5/9
print("la temperatura en celsius es de: ",c)

#5.	¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?

#a)	A = input(nombre, “¿Cuál es tu canción favorita?”)
nombre = "jorge" 
a= input(nombre, "¿cual es tu cancion favorita?")
#b)	precio = input(“Precio: “)
precio = int(input("Precio: "))
#total = precio + (precio * 0.1)
"print(total)"
#c)	edad = int(input(“Edad: “))
#print(tu edad es, edad)
"print(""tu edad es", "edad)"
#d)	edad = int(input(“Edad: “))
#print(“Veamos si tu edad es 18…”, edad=18)
"print(veamos si tu edad es 18...","edad=18"")"

#6.	Calcular la media de tres números pedidos por teclado.

n1 = int(input("numero 1: "))
n2 = int(input("numero 2: "))
n3 = int(input("numero 3: "))
print("la media de los 3 numeros es: ", (n1+n2+n3)/3)

#7.	Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

min= int(input("ingrese los minutos para saber cuantas horas son"))
h = min/60
print(float(min," minutos, son ",h, "horas"))

#8.	Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

base = int(input("ingrese su sueldo base"))
ventas = int(input("ingrese la cantidad de las ventas "))
extra = ventas*0.10
sueldo = base + extra
print("el sueldo total es de, $",sueldo)

#9.	Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.


#10.	Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
#•	    55% del promedio de sus tres calificaciones parciales.
#•	    30% de la calificación del examen final.
#•	    15% de la calificación de un trabajo final.

#11.	Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

#12.	Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica.

#13.	Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32.

#14.	Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.



