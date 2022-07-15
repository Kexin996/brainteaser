#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 12:09:09 2022

@author: zhangkexin
"""

"""
Jul 15: Brainteaser 
Extention
---------
Can we generalize the apple and drivers problem?

We define:
    
    apple: the total number of apples 
    (in this function we define apples as a multiple of distance d)
    d: the total distance 
    carry: the maximum bananas the driver can carry
    
    
    current_apple: current amount of apple
    

    formula for the amount left (also the distance of the final drop point):
        P(x) = P(x-1)+ carry / (current_apple / carry)
""" 

def left(apple,carry,d):
    l = 0
    current_apple = apple
    while (current_apple / carry != 1):
        l = l+carry / (current_apple / carry)
        current_apple -=carry

    return l


# test case
print(left(3000,1000,1000))
print(left(4000,1000,1000))