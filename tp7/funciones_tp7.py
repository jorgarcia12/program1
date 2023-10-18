#Bubble Sort

def bubble_sort(num_list):
    n = len(num_list)
    for i in range(n):
        intercambio = False
        for j in range(0, n-i-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
                intercambio = True
        if not intercambio:
            break

#Selection Sort

def selection_sort(num_list):
    n = len(num_list)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if num_list[j] < num_list[min_index]:
                min_index = j
        num_list[i], num_list[min_index] = num_list[min_index], num_list[i]

#Insertion Sort

def insertion_sort(num_list):
    for i in range(1, len(num_list)):
        key = num_list[i]  
        j = i - 1  
        while j >= 0 and key < num_list[j]:
            num_list[j + 1] = num_list[j]
            j -= 1
        num_list[j + 1] = key

#Merge Sort

def merge_sort(num_list):
    if len(num_list) > 1:
        mid = len(num_list) // 2
        left_half = num_list[:mid]
        right_half = num_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                num_list[k] = left_half[i]
                i += 1
            else:
                num_list[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            num_list[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            num_list[k] = right_half[j]
            j += 1
            k += 1

#ejercicio_3

def book_sort(book):
    return book["publicacion"]

#ejercicio_5

def bubble_sort_reverse(num_list):
    n = len(num_list)
    for i in range(n):
        intercambio = False
        for j in range(0, n-i-1):
            if num_list[j] < num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
                intercambio = True
        if not intercambio:
            break

#ejercicio_6
#ordenamiento por conteo
def counting_sort(arr):
    max_value = max(arr)  
    min_value = min(arr)  
    range_of_values = max_value - min_value + 1
    count = [0] * range_of_values
    for num in arr:
        count[num - min_value] += 1
    sorted_arr = []
    for i in range(range_of_values):
        for j in range(count[i]):
            sorted_arr.append(i + min_value)
    return sorted_arr