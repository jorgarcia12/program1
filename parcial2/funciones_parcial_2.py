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
    

    #FORMA HORIZONTAL
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
    # Vamos buscando y comparando los caracteres en las columnas para encontrar 4 iguales, cuando los encontramos los agregamos a la lista vertical_aux para luego poder compararlos con las cadenas en mutant_sequence
    # Finalmente comparamos las secuencias de adn mutante con las cadenas en vertical_aux, si estas coinciden se incrementa dna_counter
    vertical_aux = []
    for i in range(6):
        column_aux = "".join([row[i] for row in dna_list])
        for j in range(len(column_aux) - 3):
            column_aux_2 = column_aux[j:j+4]
            if column_aux_2 in mutant_sequence:
                vertical_aux.append(column_aux_2)

    # Comparamos con mutant_sequence
    for sequence in vertical_aux:
        if sequence in mutant_sequence:
            dna_counter += 1
    

    #FORMA DIAGONAL
    
    #Diagonal principal
    #Recorremos de forma que nos tome los caracteres en la diagonal principal, luego, comparamos que el siguiente caracter sea igual al anterior hasta llegar a 4 iguales, si se cumple esa condicion, los guardamos en una lista auxiliar y los comparamos con mutant_sequence
    diagonal_aux = []
    diagonal_count = 0
    for i in range(len(dna_list)):
        for j in range(len(dna_list[0])):
            #Buscamos las diagonales de izq a derecha hacia abajo y las agregamos a diagonal_aux para poder compararlas con mutant_sequence
            if i + 3 < len(dna_list) and j + 3 < len(dna_list[0]):
                diagonal_sequence = "".join([dna_list[i + l][j + l] for l in range(4)])
                if diagonal_sequence in mutant_sequence:
                    diagonal_count += 1
                    diagonal_aux.append(diagonal_sequence)        
            #En esta seccion analizamos las diagonales de derecha a izquierda hacia abajo y las agregamos a diagonal_aux para poder compararlas con mutant sequence
    for i in range(len(dna_list)):
        for j in range(len(dna_list[0])):
            if i + 3 < len(dna_list) and j - 3 >= 0:
                diagonal_sequence = "".join([dna_list[i + l][j - l]for l in range(4)])
                if diagonal_sequence in mutant_sequence:
                    diagonal_count += 1
                diagonal_aux.append(diagonal_sequence)    
    #Si encontramos una cadena de ADN en forma diagonal, aumentamos dna_counter
    if diagonal_count>=1:
            dna_counter += 1
    
    #Revisamos el contador para poder chequear que seamos mutantes o humanos
    if dna_counter>1:
        return True
    else:
        return False
    
    