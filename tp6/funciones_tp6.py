import random
#ejercicio_6

def all_names(primary_names,secundary_names,all_names):
    bonded = set(primary_names).union(secundary_names)
    all_names = list(bonded)
    return all_names

def repeated_names(primary_names,secundary_names,repeat_list):
    for i in range(len(primary_names)):
        for j in range(len(secundary_names)):
            if primary_names[i] == secundary_names[j]:
                repeat_list.append(primary_names[i])
    return repeat_list

def non_repeated_names(primary_names,secundary_names,no_repeat_list):
    no_repeat_list = list(set(primary_names) ^ set(secundary_names))
    return no_repeat_list

#ejercicio_10
def main_diagonal(matriz):
    dim = len(matriz)
    return [matriz[i][i] for i in range(dim)]

def reverse_diagonal(matriz):
    dim = len(matriz)
    return [matriz[i][dim - 1 - i] for i in range(dim)]