#Split in Half
#Given a string. Split it into two equal parts. Swap these parts and return the result.
#If the string has odd characters, the first part should be one character greater than the second part.
#Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.


def half_swap_string(s):
    if len(s)%2 == 0:
        string_1 = s[:len(s)//2]
        string_2 = s[len(s)//2:]
        result = string_2 + string_1
        return result
    else:
        string_1 = s[:(len(s)//2)+1]
        string_2 = s[(len(s)//2)+1:]
        result = string_2 + string_1
        return result


test_even = 'bbbbaaaa'
test_even_result = half_swap_string(test_even)
print(test_even_result)

test_odd = 'aaaaazzzz'
test_odd_result = half_swap_string(test_odd)
print(test_odd_result)

# time complexity for above code is O[1]

#Unique Characters in String
#Given a string, determine if it consists of all unique characters.
#For example, the string 'abcde' has all unique characters and should return True.
#The string 'aabcde' contains duplicate characters and should return False.


def unique_character(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True


unique_string = 'wor1123d'
unique_string_result = unique_character(unique_string)
print(unique_string_result)


#time complexity for this code is o[n]+o[n]???






