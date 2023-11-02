#Creamos la matriz con las 36 letras
def create_matrix():
    dna_list = []
    string_count = 0
    while string_count < 6: 
        dna_chain = input("Ingrese una base nitrogenada: ").upper()
        if check_char_chain(dna_chain):
            if chain_length(dna_chain):
                dna_list.append(dna_chain)
                string_count += 1
            else:
                print("Ingrese una base valida")
        else:
            print("Ingrese una cadena valida")
    return dna_list

#Revisamos q los caracteres ingresados sean los correctos
def check_char_chain(dna_chain):
        for i in range(len(dna_chain)):
            if dna_chain[i] != 'A' and dna_chain[i] != 'C' and dna_chain[i] != 'G' and dna_chain[i] != 'T':
                return False
        return True

#Chequeamos que el array sea tenga 6 caracteres

def chain_length(dna_chain):
    if (len(dna_chain)==6):
        return True
    else:
        return False

#Creamos una funcion para verificar si el adn ingresado es o no mutante

def is_mutant(dna_list):
    mutant_sequence = ["AAAA", "CCCC", "GGGG", "TTTT"]
    dna_counter = 0
    aux = 0
    appareances = 0
    #primero chequeamos de manera horizontal
        #Iteramos 4 veces para q compare las 4 secuencias de mutante
        #Iteramos sobre las filas y columnas para encontrar secuencias de ADN mutante
        #Usamos join para que junte la secuencia mutante con la ingresada y compare si hay 4 letras iguales e incrementamos el contador de adn
    for h in range(4):
        for i in range(6):
            for j in range(len(dna_list)):
                if mutant_sequence[h] in "".join(dna_list[j]):
                    dna_counter += 1
    #FORMA VERTICAL
    # Generamos una lista auxiliar para que nos vaya guardando los caracteres y asi poder compararlo con la secuencia mutante
    # Creamos una variable auxiliar y le damos el valor de i para q pueda comparar los otros caracteres y poder saber si hay 4 iguales en una columna
    # iteramos por la matriz en busqueda de los 4  caracteres iguales, y si aparecen los 4, los ingresamos en la lista auxiliar
    # finalmente comparamos las secuencias de adn mutante con las cadenas en vertical_aux, si estas coinciden se incrementa dna_counter
    vertical_aux = []
    for i in range(5):
        aux = dna_list[i]
        char_counter = 1
        for j in range(6):
            if dna_list[i][j]==aux:
                char_counter += 1
            else:
                char_counter = 1
            if char_counter==4:
                vertical_aux.append(aux*4)
    print(vertical_aux)
    print(mutant_sequence)
    for h in range(4):
        if mutant_sequence[h] == vertical_aux:
            dna_counter += 1 
    #Forma Diagonal

    #Regresamos el contador para poder chequear que seamos mutantes o humanos
    return dna_counter