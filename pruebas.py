#Escribir una consigna apropiada para la siguiente funcion
def f (n):
    s = str(n)
    if len(s) <= 1:
        return s
    return s[-1] + f(int(s[:-1]))

n = int(input("Ingrese un numero entero: "))

print (f"{f(n)}")

