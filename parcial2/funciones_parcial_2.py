#Creamos la matriz con las 36 letras
def create_matrix():
    dna_list = []
    string_count = 0
    while string_count < 6: 
        dna_chain = input("Ingrese una base nitrogenada: ").upper()
        if check_char_chain(dna_chain):
            if chain_length(dna_chain):
                dna_list.append(dna_chain)
                string_count = string_count + 1
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
    dna_counter = 0
    #primero chequeamos de manera horizontal
    for i in range(len(dna_list)):

    #forma horizontal

    #Forma Diagonal
