first = int(input("Introduzca el primer numero: "))
second = int(input("Introduzca el segundo numero: "))
for i in range(first,second + 1):
    if (i % 2 == 0):
        print(f"{i} es par")
    else:
        print(f"{i} es impar")

