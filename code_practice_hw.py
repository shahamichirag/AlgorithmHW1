import math

#Compute the sum of digits in all numbers from 1 to n. When a user enters a number n, find the sum of digits in all numbers from 1 to n.
#Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

def add_digits(n):
    result = 0
    for i in range(1, n+1):
        result = result + i
        i += 1
    return result


result_1 = add_digits(5)
print(result_1)
#NOTE: THE TIME COMPLEXITY FOR ABOVE PROGRAM IS O(n)

#Find max number from 3 values, entered manually from a keyboard.
#Example: 124, 21, 32. Result = 124.


def max_number(n1, n2, n3):
    result = n1
    if n2 > n1:
        result = n2
        if n3 > result:
            result = n3
    elif n2 == n1:
        result = n2
        if n3 > result:
            result = n3
    elif n2 == n3:
        if n2 > n1:
            result = n2
    elif n1 == n3:
        if n2 > n1:
            result = n2
    elif n1 == n2 == n3:
        result = n1
    else:
        result = n1
    print(f'The greatest number is {result}')


n1 = input('Please enter first number : ')
n2 = input('Please enter second number : ')
n3 = input('Please enter third number : ')
max_number(n1,n2,n3)

#NOTE: THE TIME COMPLEXITY FOR ABOVE PROGRAM IS O(1)


#Count odd and even numbers. Count odd and even digits of the whole number.
#Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).


def even_vs_odd(string):
    even_count, odd_count = 0,0
    for digit in [int(i) for i in string]:
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print(f'The number of even digit are: {even_count} \n The number of odd digits are: {odd_count}')


even_vs_odd('11111')

#NOTE: THE TIME COMPLEXITY FOR ABOVE PROGRAM IS O(n)


#Factorial n with edge cases:

def factorial(n):
    result = 1
    if n > 0:
        for i in range(1, n + 1):
            result = result * i
            i += 1
        print(result)
    elif n == 0:
        print('Factorial of zero is one')
    else:
        print('Factorial of negative number can not be define!')


factorial(-3)

#NOTE: THE TIME COMPLEXITY FOR ABOVE PROGRAM IS O(n)

#Fibonacci sequence with edge cases

def fibonacci(n):
    if n < 0:
        print('Fibonacci sequence can not be evaluate for negative numbers!')
    elif n == 0 or n ==1 or n == 2:
        print('Not enough data to produce a fibonacci sequence!')
    else:
        fib_1 = 1
        fib_2 = 1
        index = 3
        cur_result = [fib_1, fib_2]
        while index <= n:
            cur_result.append(fib_1 + fib_2)
            fib_1, fib_2 = fib_2, fib_1+ fib_2
            index = index + 1
        return cur_result


terms_result = fibonacci(4)
print(terms_result)








