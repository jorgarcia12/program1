import funciones_parcial_2
#Creamos la funcion que va a crear la matriz y verificar que los caracteres sean correctos
dna_list = funciones_parcial_2.create_matrix()
#Le mostramos la matriz ingresada al usuario
print(dna_list)
#Chequeamos mediante la funcion booleana is_mutant si el ADN ingresado es de un mutante o un humano
if (funciones_parcial_2.is_mutant(dna_list)):
    print("Felicitaciones Usted es un mutante, bienvenido al ejercito de Magneto")
else:
    print("Usted es un humano")
#MATRIZ MUTANTE
#dna_list = ['ATGCGA', 'CAGTGC', 'TTATGT', 'AGAAGG', 'CCCCTA', 'TCACTG']
#MATRIX NO MUTANTE
#dna_list = ['ACGTGA', 'CGACTT', 'ACGTGA', 'CAGATT', 'TAGATA', 'AGATTA']  