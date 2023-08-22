
consumo = int(input("Ingrese cuantos kilometros puede hacer su moto con un litro de nafta "))
tanque = int(input("Ingrese cuantos litros tiene el tanque de nafta "))
km = int(input("Ingrese la cantidad de kilometros a recorrer "))
total_tanques = km / (consumo * tanque)
print("usted necesitara ", total_tanques, "tanques para recorrer ",km," kilometros")
