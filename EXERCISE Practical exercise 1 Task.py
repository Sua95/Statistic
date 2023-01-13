# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:17:56 2019

@author: giles
"""

'''
Question 1

Create a class to represent a bank account. It will need to have a balance,
a method of withdrawing money, depositing money and displaying the balance to
the screen. Create an instance of the bank account and check that the methods
work as expected.
'''

class BankAccount(object):
    
    def __init__(self, balance=0):
        self.balance = balance
        
    def print_balance(self, balance):
        print(f'This is your balance ${balance}')
        
    def make_deposit(self):
        deposit = float(input('How much would you like to deposit?' ))
        self.balance += deposit
        print(f"Balance is now in ${self.balance}")
    
    def make_withdrawal(self):
        withdrawal = float(input('How much would you like to withdrawal?: '))
        if withdrawal > self.balance:
            print("Sorry, you don't have that amount, your current balance is {self.balance}")
        else:
            self.balance -= withdrawal
            print(f"Balance is now in ${self.balance}")
        

#sua_bbva = BankAccount(100)

#sua_bbva.make_deposit()
#sua_bbva.make_withdrawal()



'''
Question 2
 Create a circle class that will take the value of a radius and
 return the area of the circle
'''

class Circle(object):
    
    def __init__(self, radius):
        self.radius = radius
        
    def Area_Circle(self):
        a = 3.14 * self.radius ** 2
        print(f'The area of a circle with a radius of {self.radius} is {a}')
        
        
        
earth = Circle(6371)

earth.Area_Circle()
        
        
        
        
        


































