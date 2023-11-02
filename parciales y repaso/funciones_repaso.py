#Creamos el carton
def create_card(bingo_nums,num_count):
    while num_count<25:
        n = int(input("Ingrese un numero a su carton: "))
        if check_range(n):
            if n not in bingo_nums:
                bingo_nums.append(n)
                num_count = num_count + 1
            else:
                print("El numero esta repetido, ingrese otro")
        else:
            print("Ingrese un numero dentro del rango 1-75")
    return bingo_nums
#Chequeamos que el numero este entre el rango predeterminado
def check_range(n):
    if n>0 and n<75:
        return True
    else:
        return False
#Revisamos que no se repita ningun numero en la lista
def check_repeats(bingo_nums):
    if len(bingo_nums) == len(set(bingo_nums)):
        return True
    else:
        return False 
#comparamos el numero de la bolilla con el carton
def check_card(bingo_nums,bingo_all_numbers):
    for i in range(len(bingo_all_numbers)):
        if bingo_all_numbers[i] in bingo_nums:
            bingo_nums.remove(i)


