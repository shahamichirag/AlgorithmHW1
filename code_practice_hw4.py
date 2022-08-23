#Even First
#Your input is a list of integers, and you have to reorder its entries so that the even entries appear first. You are required to solve it without allocating additional storage (operate with the input list).
#Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

def even_odd_list(arr):
    result1 = []
    result2 = []
    for n in arr:
        if n % 2 == 0:
            result1.append(n)
        else:
            result2.append(n)
    return result1+result2


list1 = [7, 3, 5, 6, 4, 10, 3, 2]
result1 = even_odd_list(list1)
list2 = [3, 3, 3, 3, 2, 2, 2, 2]
result2 = even_odd_list(list2)
print(result1)
print(result2)

#Increment a Number
#Write a program that takes as input a list of digits encoding a non-negative decimal integer D and updates the list to represent the integer D + 1.
#For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].


def increment_number(arr):
    index = len(arr) - 1
    while index >= 0 and arr[index] == 9:
        arr[index] = 0
        index -= 1
    if index < 0:
        arr.insert(0, 1)
    else:
        arr[index] += 1


digits = [1, 2, 9]
increment_number(digits)
for digit in digits:
    print(digit, end=' ')










