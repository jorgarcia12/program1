
"MIRAR EJERCICIOS 10 Y 13"

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

total = int(input("ingrese el total de su compra"))
desc = total*0.15
fin = total - desc
print("su total fue de $",total, "descontando el 15%, usted debe pagar $",fin)

#10.	Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:

#•	    55% del promedio de sus tres calificaciones parciales.
#•	    30% de la calificación del examen final.
#•	    15% de la calificación de un trabajo final.

#11.	Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).
num1= int(input("ingrese el primer numero "))
num2= int(input("ingrese el segundo numero "))
dist = abs (num1 - num2)
print("la distancia entre ",num1," y ",num2," es de ",dist," lugares")

#12.	Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica.

num = int(input("ingrese un un numero para conocer su raiz cuadrada y su raiz cubica: "))
rcuad = int(num**(1/2))
rcub = int(num**(1/3))
print("la raiz cuadrada de ",num," es: ",rcuad," y la raiz cubica es:",rcub)

#13.	Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32.
num = input("Ingrese un numero para verlo dado vuelta")
num = print([-1])
#14.	Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.

num1 = str(input("iingrese un numero para la primer variable"))
num2 = str(input("iingrese un numero para la segunda variable"))
print(str.replace (num1,num2))


#15.	Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.

hh = int(input("Ingrese la hora de partida de la ciudad A: "))
mm = int(input("Ingrese el minuto de partida: "))
ss = int(input("Ingrese el segundo de partida: "))
t = int(input("Ingrese los segundos de viaje hasta la ciudad B: "))
inicio_horas = hh + mm/60 + ss/3600
fin_horas = inicio_horas + t/3600
hora_fin = int(fin_horas)
print(f"La hora de llegada a la ciudad B va a ser a las {hora_fin} horas")

#16.	Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

nombre = input("Ingrese su nombre: ")
apellido1 = input("Ingrese su primer apellido: ")
apellido2 = input("Ingrese su segundo apellido: ")
inicial_nombre = nombre[0] 
inicial_apellido1 = apellido1[0]
inicial_apellido2 = apellido2[0]
print (inicial_nombre,",",inicial_apellido1,",",inicial_apellido2)

#17.	Solicitar al usuario que ingrese su nombre. El nombre se debe almacenar en una variable llamada usuario. A continuación mostrar por pantalla: “Ahora estás en la matrix, [nombre del usuario]”.

usuario = input("Ingrese su nombre: ")
print("Ahora estás en la matrix ",usuario)

#18.	Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante. A ese valor, sumarle un 6.2% en concepto de servicio y un 10% de propina. Imprimir en pantalla el monto final a pagar.

costo_cena = float(input("Ingrese cuanto costo la cena: "))
monto_final = costo_cena + costo_cena * 0.062 + costo_cena * 0.1
print("El monto final a pagar considerando servicio y propina es de $",monto_final)

#19.	Solicitar al usuario que ingrese el día, mes y año de su nacimiento y almacenar cada uno de ellos en una variable numérica (en total, tres variables diferentes). Finalmente, mostrar la fecha en formato dd/mm/aaaa.

dia = int(input("Ingrese el numero de su dia de nacimiento: "))
mes = int(input("Ingrese el numero de su mes de nacimiento: "))
an = int(input("Ingrese su año de nacimiento: "))
print("Fecha de nacimiento:" ,dia,"/",mes,"/",an)

#20.	Hacer otra versión del programa, pero esta vez almacenado todo en una única variable con formato DDMMAAA.

ddmmaa = int(input("Ingrese su fecha de nacimiento en forma numerica DDMMAAA: "))
digito1_anio = str(ddmmaa % 10)
ddmmaa = int(ddmmaa / 10)
digito2_anio = str(ddmmaa % 10)
ddmmaa = int(ddmmaa / 10)
digito3_anio = str(ddmmaa % 10)
ddmmaa = int(ddmmaa / 10)
digito4_anio = str(ddmmaa % 10)
ddmmaa = int(ddmmaa / 10)
digito1_mes = str(ddmmaa % 10)
ddmmaa = int(ddmmaa / 10)
digito2_mes = str(ddmmaa % 10)
ddmmaa = int(ddmmaa / 10)
digito1_dia = str(ddmmaa % 10)
ddmmaa = int(ddmmaa / 10)
digito2_dia = str(ddmmaa)
anio = digito4_anio + digito3_anio + digito2_anio + digito1_anio
mes = digito2_mes + digito1_mes
dia = digito2_dia + digito1_dia
print("Su fecha de nacimiento es: ", dia,"/",mes,"/",anio)

#21.	Una pareja de motociclistas necesita hacer ciertos cálculos antes de emprender un viaje en moto, para saber cuántos tanques de combustible consumirá el viaje entero. 
    # Para eso deben ingresar: cuántos kilómetros puede recorrer su moto con 1 litro de combustible, qué capacidad (en litros) tiene el tanque y cuántos kilómetros en total recorrerán.
    # Hacer un programa que solicite los datos necesarios y luego informe la cantidad de tanques de combustible necesarios.

consumo = int(input("Ingrese cuantos kilometros puede hacer su moto con un litro de nafta "))
tanque = int(input("Ingrese cuantos litros tiene el tanque de nafta "))
km = int(input("Ingrese la cantidad de kilometros a recorrer "))
total_tanques = km / (consumo * tanque)
print("usted necesitara ", total_tanques, "tanques para recorrer ",km," kilometros")

