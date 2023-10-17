import funciones
#1. Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente forma: (nombre, dni, destino). Por ejemplo:
#*(‘Manuel Juarez’, 12345678, ‘San Juan’), (‘Silvana Paredes’, 62258472, ‘Mendoza’)+

#Además en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo:
#*(‘Buenos Aires’, ‘Argentina’), (‘Lisboa’, ‘Portugal’), (‘Mendoza’, ‘Argentina’)+
#Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:

#- Agregar pasajeros a la lista de viajeros.
#- Agregar ciudades a la lista de ciudades.
#- Dado el DNI de un pasajero, ver a qué ciudad viaja.
#- Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
#- Dado el DNI de un pasajero, ver a qué país viaja.
#- Dado un país, mostrar cuántos pasajeros viajan a ese país.
#- Salir del programa.


passenger_list = []
cities_list = []

while True:
    print("\nMenú:")
    print("1. Agregar pasajeros")
    print("2. Agregar ciudades")
    print("3. Dado el DNI de un pasajero, ver a qué ciudad viaja")
    print("4. Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad")
    print("5. Dado el DNI de un pasajero, ver a qué país viaja")
    print("6. Dado un país, mostrar cuántos pasajeros viajan a ese país")
    print("7. Salir")

    option = int(input("Ingrese la opción deseada: "))


    if option == 1:
        name = input("Nombre del pasajero: ")
        dni = int(input("DNI del pasajero: "))
        destiny = input("Destino del pasajero: ")
        passenger_list.append((name, dni, destiny))

    elif option == 2:
        city = input("Ciudad: ")
        country = input("País de la ciudad: ")
        cities_list.append((city, country))

    elif option == 3:
        dni = int(input("Ingrese el DNI del pasajero: "))
        found = False
        for pasajero in passenger_list:
            if pasajero[1] == dni:
                destiny_city = pasajero[2]
                found = True
                break
        if (found):
            print(f"El pasajero viaja a {destiny_city}")
        else:
            print("DNI no encontrado")

    elif option == 4:
        city = input("Ingrese una ciudad: ")
        city = city.lower()
        travelers_counter = 0
        for i in passenger_list:
            if (i[2] == city):
                travelers_counter += 1
        print(f"La cantidad de pasajeros que viajan a {city} es {travelers_counter}")

    elif option == 5:
        dni = int(input("Ingrese el DNI del pasajero: "))
        found = False
        for passager in passenger_list:
            if passager[1] == dni:
                destiny_city = passager[2]
                found = True
                break
        if (found):
            for city, country in cities_list:
                if city == destiny_city:
                    print(f"El pasajero va a viajar a {country}")
                    break
        else:
            print("DNI no encontrado")

    elif option == 6:
        country = input("Ingrese un país: ")
        country = country.lower()
        country_passager_counter = 0
        for i in cities_list:
            if (i[1] == country):
                country_passager_counter += 1
            else:
                pass
        print(f"La cantidad de pasajeros que viajan a {country} es {country_passager_counter}")

    elif option == 7:
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")


#2. Suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, la cual contiene tuplas con información de cada venta: (cliente, día del mes, monto, domicilio del cliente). Ejemplo:
#*(‘Nuria Costa’, 5, 1234.5,’Calle 1 – 456’), (‘Jorge Russo’, 7, 3999, ‘Calle 2 – 741’)+ Escribir una función que reciba como parámetro una lista con el formato mencionado anteriormente y retorne los domicilios de cada cliente al cual se le debe enviar una factura de compra. Notar que cada cliente puede haber hecho más de una compra en el mes, por lo que la función debe retornar una estructura que contenga cada domicilio una sola vez.

buy_list = [("Nuria Costa",5,1234.5,"Calle 1 - 456"),("Jorge Russo",7,3999,"Calle 2 - 741"),("Nuria Costa",10,345,"Calle 1 - 456"),("Matias Games",23,3678,"Calle 3 - 678")]
home_list = funciones.home(buy_list)
print("Los domicilios de las personas que se les debe enviar una factura de compra son: ")
for i in home_list:
    print(i)

#3. Crear un programa para gestionar datos de los socios de un club, permitiendo:
# - Cargar información de los socios en un diccionario para acceder por número de socio. Los datos a almacenar son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al día (s/n). El programa debe iniciar con los datos de los socios fundadores ya cargados:
#o Socio n°1, Amanda Núñez, ingresó: 17/03/2009, cuota al día.
#o Socio n°2, Bárbara Molina, ingresó: 17/03/2009, cuota al día.
#o Socio n°3, Lautaro Campos, ingresó: 17/03/2009, cuota al día.
#- Informar cantidad de socios del club.
#- Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas adeudadas.
# - Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, para indicar que en realidad ingresaron el 14/03/2018.
# - Solicitar el nombre y apellido de un socio y darle de baja (eliminarlo del listado)
# - Imprimir el listado de socios completo.


partner_dictionary = {1:[1,"Amanda Nùñez","17/03/2009","s"],2:[2,"Bárbara Molina","17/03/2009","s"],3:[3,"Lautaro Campos","17/03/2009","s"]}
partner_list = []
while True:
    partner_number = int(input("Ingrese el numero de socio del club: "))
    partner_list.append(partner_number)
    name = input("Ingrese el nombre: ")
    name = name.lower()
    partner_list.append(name)
    date_income = input("Ingrese la fecha de ingresa en formato dd/mm/aaaa: ")
    partner_list.append(date_income)
    share_at_day = input("Ingrese s si tiene la cuota al dia y n si no: ")
    share_at_day = share_at_day.lower()
    partner_list.append(share_at_day)
    partner_dictionary[partner_number] = partner_list
    partner_list = []
    out = input("Ingrese 0 para salir o cualquier otra tecla para continuar ingresando datos: ")
    if (out == "0"):
        break
    else:
        pass
print(f"La cantidad de socios del club es {len(partner_dictionary)}")
partner_number = int(input("Introduzca un numero de socio para saber si tiene todas las cuotas al dia: "))
for key,value in partner_dictionary.items():
    if (partner_number == key):
        if (value[3] == "s"):
            print("Tiene la cuota al dia")
        else:
            print("No tiene la cuota al dia")
    else:
        pass

for value in partner_dictionary.values():
    if (value[2] == "13/03/2018"):
        value[2] =  "14/03/2018"
    else:
        pass

name = input("Ingrese el apellido y nombre del socio que quiera darle de baja: ")
name = name.lower()

for value in partner_dictionary.values():
    if (value[1].lower() == name):
        del partner_dictionary[value[0]]
        break
    else:
        pass 


print("El listado de socios completo es:")

for values in partner_dictionary.values():
    print(f"Socio Nro {values[0]}: {values[1]}")