# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:15:24 2019

@author: giles
"""

# Exercises

'''
Question 1
Create a function that will calculate the sum of two numbers. Call it sum_two.
'''

x, y = 3, 5

def sum_of_two(x, y):
    result = x + y
    return result

#print(sum_of_two(x, y))

'''
Question 2
Write a function that performs multiplication of two arguments. By default the
function should multiply the first argument by 2. Call it multiply.
'''

def multiply(x, y=0):
    if not y:
        return x * 2
    else:
        return x * y
        
#print(multiply(x))


'''
Question 3
Write a function to calculate a to the power of b. If b is not given
its default value should be 2. Call it power.
'''

def power(number_a, number_b=2):
    return number_a ** number_b
    
#print(power(x))


'''
Question 4
Create a new file called capitals.txt , store the names of five capital cities
in the file on the same line.
'''

with open("capitals.txt", "w") as new_text:
    new_text.write("Argentina: Buenos Aires  \n" )
    new_text.write("Chile: Santiago  \n")
    new_text.write("Colombia: Bogota  \n")
    new_text.write("Costa Rica: San Jose  \n")
    new_text.write("Mexico: Ciudad de Mexico  \n")
    

'''
Question 5
Write some code that requests the user to input another capital city.
Add that city to the list of cities in capitals. Then print the file to
the screen.
'''

def add_cities(text):
    new_capitals = input('Cual es la ciudad y capital? ')
    with open(text, "a") as txt:
        txt.write(new_capitals)
        
add_cities("capitals.txt")
    


'''
Question 6
Write a function that will copy the contents of one file to a new file.
'''

def copy_text(file_1, file_2):
    with open(file_1, 'r') as f1:
        with open(file_2, 'w') as f2:
            f2.write(f1.read())
            
            
copy_text("capitals.txt", "new_text.txt")
    




