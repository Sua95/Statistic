# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 17:32:12 2019

@author: giles
"""


import math

dictionary =  {'c': 15, 'o': 22, 'n': 19, ' ': 36, 'l': 14, 'a': 19, 'b': 2, 'm': 1, 'ó': 2, 'v': 2, 'i': 18, 's': 16, 't': 8, 'u': 7, 'e': 20, 'f': 4, 'r': 10, 'p': 6, 'd': 7, ',': 3, 'y': 1, 'z': 1, 'é': 1, 'g': 1, '.': 1}
{'c': 15, 'o': 22, 'n': 19, 'l': 14, 'a': 19, 'b': 2, 'm': 1, 'ó': 2, 'v': 2, 'i': 18, 's': 16, 't': 8, 'u': 7, 'e': 20, 'f': 4, 'r': 10, 'p': 6, 'd': 7, 'y': 1, 'z': 1, 'é': 1, 'g': 1}



'''
Question 1
Can you remember how to check if a key exists in a dictionary?
Using the capitals dictionary below write some code to ask the user to input
a country, then check to see if that country is in the dictionary and if it is
print the capital. If not tell the user it's not there.
'''

#user_key = input('Wich letter you want to find? ')

def find_key(dictionary, user_key):
    input_lower = user_key.lower()
    if input_lower in dictionary:
        print(f'{input_lower} is on the dictionary with {dictionary.get(input_lower)}V instances')
    else:
        print(f'{input_lower} in not on dictionary')
        


'''
Question 2
Write python code that will create a dictionary containing key, value pairs
that represent the first 12 values of the Fibonacci sequence
i.e {1:0,2:1,3:1,4:2,5:3,6:5,7:8 etc}
'''
def fibonacci_dict():
    fibonacci = [0, 1]
    dict_fibonacci = {}
    for i in range(11):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
        
    for i in range(len(fibonacci)):
        dict_fibonacci[i] = fibonacci[i]
                
    print(dict_fibonacci)

    


'''
Question 3
Create a dictionary to represent the open, high, low, close share price data
for 4 imaginary companies. 'Python DS', 'PythonSoft', 'Pythazon' and 'Pybook'
the 4 sets of data are [12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]
'''

Companies = {'Python DS': [12.87, 13.23, 11.42, 13.10], 
             'PythonSoft': [23.54,25.76,21.87,22.33],
             'Pythazon': [98.99,102.34,97.21,100.065],
             'Pybook': [203.63,207.54,202.43,205.24]
             }

python_DS = {"open": 12.87 ,"high": 13.23 ,"low": 11.42 , "close": 13.10}
pythonSoft = {"open": 23.54 ,"high": 25.76 ,"low": 21.87 , "close": 22.33}
pythazon = {"open": 98.99 ,"high": 25.76 ,"low": 97.21 , "close": 100.065}
pybook = {"open": 203.63 ,"high": 207.54 ,"low": 202.43, "close": 205.24}


'''
Question 4
Go to the python module web page and find a module that you like. Play with it,
read the documentation and try to implement it.
'''

an_int = 12
a_float = 10

factorial = math.factorial(7)


'''
Question 5
Create a dictoinary containing as keys the letters from A-Z, the values should
be random numbers created from the random module. Can you draw a bar graph of
the results?
'''

import string as st
import random as rn
import matplotlib.pyplot as plt

alphabet = list(st.ascii_lowercase)

dict_alph = {}

for l in alphabet:
    dict_alph[l] = rn.randint(1, 100)
    
x, y = zip(*dict_alph.items())

plt.bar(x, y)
plt.show()



'''
Question 6
Create a dictionary containing 4 suits of 13 cards
['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
'''



