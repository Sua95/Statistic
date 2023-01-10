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

# Two if statements who compare who is the bigger number and print the differences one by one

'''
Question 2
Ask the user to input a string and then print it out to the screen in
reverse order (use a for loop).
'''

#name = input("Put your name --> ")

def print_backwards(user_string):
    for l in range(len(user_string)-1, -1, -1):
        print(user_string[l])
    
# With the triple -1 it's equal to say reversed

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
        
# The print it's inside the loop to print on every loop


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
            
# A loop inside another loop to print all times table from 1 to 12

'''
Question 5
Ask the user to input a sequence of numbers. Then calculate the mean
and print the result
'''

def mean_input():
    
# An input inside a loop then the mean formula
    user_array = []
    for i in range(5):
        user_array.append(int(input('Choose 5 numbers: ')))
        print(f'the mean is: {sum(user_array) / len(user_array)}')


'''
Question 6
Write code that will calculate 15 factorial. (factorial is product of
positive ints up to a given number. e.g 5 factorial is 5x4x3x2x1)
'''


number = 4
    
def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result
        
# i never gets 0 cause range starts in 1

'''
Question 7
Write code to calculate Fibonacci numbers. Create list containing
first 20 Fibonacci numbers, (Fib  numbers made by sum of preceeding
two. Series starts 0 1 1 2 3 5 8 13 ....)
'''


fibonacci = [0, 1]

def fibonacci_autofill(initial_array):
    
# append new values with the sum of the last 2 numbers in the array
    for i in range(19):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
        


'''
Question 8
The previous question was the first to contain comments. Go back
through the other questions in this file and add comments to the
solutions.
'''


# DONE



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

def f_in_prints():
    print("*****")
    print("*")
    print("****")
    print("*")
    print("*")
    print("*")

# Nothing to comment

'''
Question 10
Write some code that will determine all odd and even numbers
between 1 and 100. Put the odds in a list named odd and the evens
in a list named even.
'''

even_list = []
odd_list = []

def add_odds_and_evens(even_list, odd_list):
    for n in range(1,101):
        if n % 2 == 0:
            even_list.append(n)
        elif n % 2 != 0:
            odd_list.append(n)       
    print(even_list)
    print(odd_list)
    
    
# Pretty useful that .append function


























