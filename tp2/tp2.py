#1-	Crear un programa que reciba el número de años que tiene nuestra computadora y muestre en la consola que el computador es nuevo si es menor o igual a 2 años y que el computador es viejo si es mayor a 2 años.

edad_pc = int(input("Ingrese la antiguedad de su computadora: "))
if edad_pc > 2:
    print("su PC es viejo")
else:
    print("su PC es nueva")

#2-	Hacer que el programa anterior muestre un mensaje de error si el usuario digita un número negativo.

edad_pc = int(input("Ingrese la antiguedad de su computadora: "))
if edad_pc > 2:
    print("su PC es viejo")
elif edad_pc < 0:
    print("error, ingreso un numero negativo")
else:
    print("su PC es nueva")

#3-	Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables. A continuación. Imprimir ‘coincidencia’ si ambos nombres comienzan con la misma letra. Si no es así, imprimir ‘no hay coincidencia’.

nombre1 = input("Ingrese un nombre ").lower()
nombre2 = input("Ingrese un nombre ").lower()
if nombre1[0] == nombre2[0]:
    print("Coincidencia")
else:
    print("No hay coincidencia")
#4-	Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verdad, candidato C por el partido azul.Según el candidato elegido (A, B o C) se debe imprimir el mensaje: ‘Usted ha votado por el partido [color del candidato elegido]. Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar ‘Opción errónea.’
print("ELECCIONES!")
voto = input("Partido rojo (A) // Partido verde (B) // Partido azul (C): ").upper()
if voto == "A":
    print("Usted voto por el partido rojo!")
elif voto == "B":
    print("Usted voto por el partido verde!")
elif voto == "C":
    print("Usted voto por el partido azul!")
else:
    print("Opcion erronea")


#5-	Escribir un programa que solicite al usuario una letra, si es una vocal, mostrar el mensaje ‘Es vocal’.Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato.

letra = input("ingrese una letra para saber si es vocal: ").lower()

if len(letra)==1:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print("es vocal")
    else:
        print("NO es vocal")
else:
    print("Error, usted ingreso mas de un caracter")


#6-	Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.

anio= int(input("ingrese un año para saber si es bisiesto: "))

if anio % 4==0 and anio % 100 != 0 and anio % 400 != 0:
    print("Es bisiesto")
else:
    print("No es Bisiesto")
    

#7-	Escribí un programa para solicitar al usuario tres números y mostrar en pantalla al menor de los tres.

n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese un numero: "))
n3 = int(input("Ingrese un numero: "))
menor = n2
if n1 < n2:
    menor = n1
elif n1 < n3:
    menor = n3

print("el numero menor es: ",menor)

#8-	Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla “Usuario y contraseña correctos. Puede ingresar a Camelot”. Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”.

usuario = input("Ingrese el usuario: ").title()
contrasena = input("Ingrese la contraseña: ")

if usuario == "Gwenevere" and contrasena == "excalibur":
    print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
    print("Acceso denegado")

#9-	Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nombre = input("Ingrese su nombre: ").lower()
sexo = input("Ingrese su sexo (M) o (F): ").lower()
if sexo == "f" and nombre[0]<"m" or sexo == "m" and nombre[0]> "n":
    print("pertenece al grupo A")
else:
    print("pertenece al grupo B")

#10-	Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $500 y si es mayor de 18 años, $1000.

edad = int(input("Ingrese su edad: "))

if edad > 0 and edad < 4:
    print("usted puede entrar gratis")
elif edad >= 4 and edad <= 18:
    print("su entrada es de $500")
elif edad > 18:
    print("su entrada vale $1000")
else:
    print("Ingrese una edad valida")

#11-	La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
#•	Ingredientes vegetarianos: Pimiento y tofu.
#•	Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

tipo_pizza = input("Desea una pizza vegetariana? (S) || (N): ").lower()
if tipo_pizza == "s":
    ingredientes = input("agregue un ingrediente: Pimiento y tofu: (P) || (T): ").lower()
    if ingredientes == "p":
        print("Usted eligio una pizza vegetariana, con muzarrella, tomate y PIMIENTO")
    elif ingredientes == "t":
        print("Usted eligio una pizza vegetariana, con muzarrella, tomate y TOFU")
    else:
        print("ingrese una opcion valida")
elif tipo_pizza == "n":
    ingredientes = input("agregue un ingrediente: Peperoni, Jamón y Salmón (P) || (J) || (S): ").lower()
    if ingredientes == "p":
        print("Usted eligio una pizza NO vegetariana con muzarrella, tomate y PEPERONI")
    elif ingredientes == "j":
        print("Usted eligio una pizza NO vegetariana con muzarrella, tomate y JAMON")
    elif ingredientes == "s":
        print("Usted eligio una pizza NO vegetariana con muzarrella, tomate y SALMON")
    else:
        print("ingrese una opcion valida")
else:
    print("Ingrese una opcion valida")

#12-	Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.

anio1 = int(input("Ingrese un año: "))
anio2 = int(input("Ingrese un año: "))

if anio1 > anio2:
    cuantos_anios = anio1 - anio2
else:
    cuantos_anios = anio2 - anio1
print(f"Entre el año {anio1} y el año {anio2} hay {cuantos_anios} años de diferencia")

#13-	Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor. Haciendo que el programa avise cuando se escriben valores negativos o nulos.

n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese un numero: "))

if n1 > 0 and n2 > 0:
    if n1 > n2:
        if n1 % n2 == 0:
            print(f"{n1} es multiplo de {n2}")
        else:
            print("no son multiplos")
    elif n2 % n1 == 0:
        print(f"{n2} es multiplo de {n1}")
else:
    print("Ingrese numero mayores a 0")

#14-	Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba la solución.Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o que todos los números sean solución. Se recuerda que la fórmula de las soluciones es x = -b / a

a = float(input("Ingrese el coeficiente de la ecuacion de primer grado: "))
b = float(input("Ingrese el termino independiente de la ecuacion de primer grado: "))
if (a == 0 and b == 0):
    print("La ecuacion tiene infinitas soluciones")
elif (a == 0 and b != 0):
    print("La ecuacion no tiene solucion")
else:
    print(f"La solucion de la ecuacion es {-b / a}")

#15-	Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo. Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene que pedir entonces la base y la altura y escribir el área. Si se contesta que se quiere calcular el área de un círculo (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área.
import math
que_area = input("Desea calcular el area de un triangulo o un circulo? (T) || (C)").lower()
if que_area == "t":
    b = int(input("ingrese la base del triangulo: "))
    h = int(input("ingrese la altura del triangulo: "))
    area = float((b * h)/2)
    print(f"El area del triangulo es de {area}")
elif que_area == "c":
    r = float(input("Ingrese el radio del circulo: "))
    area = math.pi * (r**2)
    print (f"El area del circulo es de {area}")
else:
    print("INGRESE UNA OPCION VALIDA")
#16-	Haz una calculadora básica pida al usuario dos valores, a y b. Según la opción que desean, realizar la operación:
#•	Si operación es 1 entonces debemos ver el resultado de a + b
#•	Si operación es 2 entonces debemos ver el resultado de a * b
#•	Si operación es 3 entonces debemos ver el resultado de a - b
#•	Si operación es 4 entonces debemos ver el resultado de a / b

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

op = input("Ingrese la operacion a realizar: (S) || (R) || (M) || (D) ").lower()
if op == "s":
    print(f"La suma entre los dos numeros es: {a + b}")
elif op == "r":
    print(f"la resta entre los dos numeros es: {a- b}")
elif op == "m":
    print(f"la multiplicacion entre los dos numeros es: {a * b}")
elif op == "d":
    if (b==0):
        print("El divisor no puede ser cero")
    else:
        print(f"la division entre los dos numeros es: {a / b}")
else:
    print("ingrese una operacion valida")

#17-	Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje.

dia = input("Ingrese un dia de la semana: ").lower()
if dia == "lunes":
    print("Es lunes, buena semana!")
elif dia == "viernes":
    print("Es viernes, buen finde!")
elif dia == "sabado" or dia == "domingo":
    print("Disfrute su fin de semana")
elif dia == "martes" or dia == "miercoles" or dia == "jueves":
    print("Es dia de semana!")
else:
    print("ingrese un dia valido")

#18-	Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora. La jornada de trabajo mínima es de 48 horas. Calcular, dadas las horas trabajadas, si trabajó horas extras y mostrar esta cantidad. Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas un 10% más que las horas labor<ales comunes.

horas = int(input("Ingrese la cantidad de horas trabajadas este mes: "))
salario_hora = int(input("Ingrese cuanto cobra por hora"))

if horas > 48:
    horas_extra = horas - 48
    print(f"Usted trabajo {horas_extra} horas extra")
    salario_total = 48 * salario_hora + horas_extra * (salario_hora * 1.10)
    print(f"su salario total es de ${salario_total}")
else:
    salario_total = horas * salario_hora
    print(f"su salario total es de ${salario_total}")

#19-	Determinar cuánto se debe pagar por una cantidad de lápices considerando que si son 1000 o más, existe un descuento de 7% y teniendo en cuenta que el costo por lápiz es de $60; de lo contrario no hay descuento.

cantidad_lapices = int(input("Ingrese la cantidad de lapices q va a comprar: "))

if (cantidad_lapices > 999):
    pago = cantidad_lapices* 60
    total_desc = pago * 0.93
    
    print = (f"Con descuento, usted debe ${total_desc}")
else:
    print(f"usted debe ${cantidad_lapices*60}")

#20-	Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara si su promedio de cuatro (4) notas, es mayor o igual a 6; caso contrario saldrá desaprobado.

n1 = float(input("Ingrese la primer nota: "))
n2 = float(input("Ingrese la segunda nota: "))
n3 = float(input("Ingrese la tercera nota: "))
n4 = float(input("Ingrese la cuarta nota: "))

prom = (n1 + n2 + n3 + n4)/4
if (prom >=6 ):
    print(f"Usted aprobo con {prom}, felicidades!")
else:
    print(f"Usted desaprobo con {prom}, siga estudiando!")