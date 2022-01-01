# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 04:47:34 2022

@author: voidstar13

"""

numbers=[1,2,3,4,5,6,7,8,9]
def check_even(l1):
    
    for number in numbers:
        if number%2==0:
            #yield creates a generator object 
            yield number
            
n=check_even(numbers)

print(type(n))
for i in n:
    print(i, end=",")
        

