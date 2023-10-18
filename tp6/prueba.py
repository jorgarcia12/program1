import random
import funciones_tp6


fruits_table = {'tomate' : 10,'naranja' : 5, 'manzana' : 7, 'banana' : 8 }
print(fruits_table)
fruit_selection = input("Ingrese que fruta va a llevar: ")
kilos = int(input("Ingrese cuantos kilos va a llevar: "))
if fruit_selection in fruits_table:
    value = fruits_table[fruit_selection]
    total_price = value * kilos

print(f"Usted llevo {kilos} kilos de {fruit_selection}, su total es de ${total_price}")
