n1 = float(input("Ingrese la primer nota: "))
n2 = float(input("Ingrese la segunda nota: "))
n3 = float(input("Ingrese la tercera nota: "))
n4 = float(input("Ingrese la cuarta nota: "))

prom = (n1 + n2 + n3 + n4)/4
if (prom >=6 ):
    print(f"Usted aprobo con {prom}, felicidades!")
else:
    print(f"Usted desaprobo con {prom}, siga estudiando!")