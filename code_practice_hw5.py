#Selection sorting (Descending order)


def selection_sort(arr):
    for i in range(len(arr)): #i = 0
        min_index = i   # i = 0 i.e. 2
        for j in range(i+1, len(arr)): #j = 1
            if arr[j] > arr[min_index]: # 22> 2 ?
                min_index = j # min_index = 22
        arr[i], arr[min_index] = arr[min_index], arr[i]  # swap 2 and 22
    return arr # new list after first iteration ---> [22, 2, 222, 2222] and so on


list_1_sort = [2, 22, 222, 2222]
print(selection_sort(list_1_sort))
list_2_sort = [-10, 3.5, 55, -0.1, 100, 5]
print(selection_sort(list_2_sort))


# Bubble sorting (Descending order)


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


list_1_sort = [2, 22, 222, 2222, 2]
print(bubble_sort(list_1_sort))
list_2_sort = [0.2, 99, -1.5, 0.0001, 1, -1.5]
print(bubble_sort(list_2_sort))


#Insertion sorting (descending order)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key > arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    print(arr)


list_1_sort = [2, 22, 222, 2222, 2]
insertion_sort(list_1_sort)
list_2_sort = [0.2, 99, -1.5, 0.0001, 1, -1.5]
insertion_sort(list_2_sort)


#Merge sorting(descending order)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    first = merge_sort(arr[:middle])
    second = merge_sort(arr[middle:])
    return merge_arrays(first, second)


def merge_arrays(left_arr, right_arr):
    merged_array = []
    i = j = 0
    while i < len(left_arr) or j < len(right_arr):
        if i == len(left_arr):
            merged_array.append(right_arr[j])
            j += 1
            continue

        if j == len(right_arr):
            merged_array.append(left_arr[i])
            i += 1
            continue

        if left_arr[i] >= right_arr[j]:
            merged_array.append(left_arr[i])
            i += 1
        else:
            merged_array.append(right_arr[j])
            j += 1
    return merged_array


test_list = [1, 4, 3, 5, 2, 6, 7, 8]
result_list = merge_sort(test_list)
print(result_list)


