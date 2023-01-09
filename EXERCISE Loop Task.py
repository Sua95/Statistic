#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 08:50:32 2019

@author: Giles
"""

'''
Question 1
Ask the user for two numbers between 1 and 100. Then count from the
lower number to the higher number. Print the results to the screen.
'''

#num_one, num_two = int(input("Chose a number ")), int(input("Chose another number "))

def countin_difference(num_one, num_two):
    if num_one < num_two:
        while num_one <= num_two:
            print(num_one)
            num_one += 1
    elif num_one > num_two:
        while num_two <= num_one:
            print(num_two)
            num_two += 1



'''
Question 2
Ask the user to input a string and then print it out to the screen in
reverse order (use a for loop).
'''

#name = input("Put your name --> ")

def print_backwards(user_string):
    for l in range(len(user_string)-1, -1, -1):
        print(user_string[l])
    


'''
Question 3
Ask the user for a number between 1 and 12 and then display a times
table for that number.
'''


def multiplications_w_input():
    user_num = int(input("What times table did you want to see?: "))
    mul_array = []
    for i in range(0,10):
        mul_array.append(user_num*(i+1))
        print(f'{user_num} by {i+1} equals {user_num * (i + 1)}')
        

'''
Question 4
Can you amend the solution to question 3 so that it just prints out all
times tables between 1 and 12? (no  need to ask user for input)
'''

multiplicator = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 

def times_table(multiplicator, number):
    for mult in multiplicator:
        print(" ")
        for num in number:
            print(f'{num} x {mult} = {num * mult}', end=" ")
            

'''
Question 5
Ask the user to input a sequence of numbers. Then calculate the mean
and print the result
'''

user_array = []

for i in range(5):
    user_array.append(int(input('Choose 5 numbers: ')))
    
print(f'the mean is: {sum(user_array) / len(user_array)}')


'''
Question 6
Write code that will calculate 15 factorial. (factorial is product of
positive ints up to a given number. e.g 5 factorial is 5x4x3x2x1)
'''


'''
Question 7
Write code to calculate Fibonacci numbers. Create list containing
first 20 Fibonacci numbers, (Fib  numbers made by sum of preceeding
two. Series starts 0 1 1 2 3 5 8 13 ....)
'''



'''
Question 8
The previous question was the first to contain comments. Go back
through the other questions in this file and add comments to the
solutions.
'''

'''
Question 9

     *****
     *
     ****
     *
     *
     *
Can you draw this using python? (comment the solution code)
'''



'''
Question 10
Write some code that will determine all odd and even numbers
between 1 and 100. Put the odds in a list named odd and the evens
in a list named even.
'''
