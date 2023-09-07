how_many = int(input("Ingrese cuantos numeros va a ingresar: "))
count= 0
for i in range(how_many):
    number = int(input("Ingrese un numero: "))
    if number < 0:
        count = count + 1
print(f"Usted ingreso {count} numeros negativos")