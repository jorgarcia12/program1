#Creamos la matriz con las 36 letras
def create_matrix(l, c):
    matrix = []
    letter_count = 0
    while letter_count < 36: 
        l_aux = []  
        for i in range(l):
            for j in range(c):
                if letter_count < 36:
                    letter = input(f"Ingrese una base nitrogenada: ").upper() 
                    if check_character(letter):
                        l_aux.append(letter) 
                        letter_count += 1
                    else:
                        print("Ingrese una base nitrogenada válida")
                else:
                    break
        matrix.append(l_aux) 
    return matrix

#Revisamos q los caracteres ingresados sean los correctos
def check_character(letter):
    if letter =='A' or letter =='C' or letter =='G' or letter =='T':
        return True
    else:
        return False

#Con esta funcion le vamos a mostrar al usuario la matriz

def print_matrix(matrix):
    for l in matrix:
        for c in l:
            print(c, end= ", ")
        print("||")