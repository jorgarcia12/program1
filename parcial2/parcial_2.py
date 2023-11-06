import funciones_parcial_2
#Creamos la funcion que va a crear la matriz y verificar que los caracteres sean correctos
dna_list = funciones_parcial_2.create_matrix()
print(dna_list)
if (funciones_parcial_2.is_mutant(dna_list)):
    print("Felicitaciones Usted es un mutante, bienvenido al ejercito de Magneto")
else:
    print("Usted es un humano")
