#Below The Arithmetical Mean
#When given a list, the program should return a list of all the elements below the original list’s arithmetical mean. The arithmetical mean is the sum of all elements divided by the number of elements.
#Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]


def num_less_mean(list1):
    total = sum(list1)
    mean = total / (len(list1))
    final_list = []
    for i in range(0, len(list1)):
        if list1[i] < mean:
            final_list.append(list1[i])
            i += 1
    return final_list


list2 = [1,3,5,6,4,10,2,3]
result = num_less_mean(list2)
print(result)
list_2 = [2, 2, 2, 2, 2, 2, 2, 2]
result_2 = num_less_mean(list_2)
print(result_2)


#TIME COMPLEXITY OF ABOVE CODE IS O(N)


#The Lowest Elements
#When given a list of elements, find the lowest element.
#Example: [198, 3, 4, 9, 10, 9, 2], Return: 2


def min_numbers(l):
    min_number = l[0]
    for i in range(1, len(l)):
        if l[i] <= min_number:
            min_number = l[i]
            i += 1
    return min_number


list_2 = [198, 3, 4, 9, 10, 9, 2]
list_3 = [111,11,1,0]
result_list = min_numbers(list_2)
print(result_list)
result_list1 = min_numbers(list_3)
print(result_list1)


#THE TIME COMPLEXITY FOR ABOVE CODE IS O(n)


#Two Lowest Elements
#When given a list of elements, find the two lowest elements.
#They can be equal to each other or different.
#Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3


def two_lowest_ele(list_l):
    list_l.sort()
    print('The lowest two numbers in the lists are:', {list_l[0], list_l[1]})


list_4 = [198, 3, 4, 9, 10, 9, 2]
two_lowest_ele(list_4)
list_5 = [1111, 111, 11, 1]
two_lowest_ele(list_5)


#THE TIME-COMPLEXITY OF THE ABOVE CODE IS O(1)


