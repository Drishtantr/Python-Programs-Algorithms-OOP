# -*- coding: utf-8 -*-
"""
Created on Mon May 25 13:05:26 2020

@author: nilima
"""

def logic(my_input):
     product=1
     for item in my_input:
         if item.isnumeric(): #checks whether a string is numeric or not
             product *= int(item)
         else:
             continue
     return product
my_input = input("Enter a string:")
print(logic(my_input))
