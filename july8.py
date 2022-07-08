#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 11:06:45 2022

@author: zhangkexin
"""

"""
Jul 8: Brainteaser 
Extention
---------
Can we generalize the process of pouring water back and forth?

We define:
    C_w1: the concentration of water in water jug
    C_a1: the concentration of alcohol in water jug 
    
    C_w2: the concentration of water in alcohol jug
    C_a2: the concentration of alcohol in alcohol jug
    *** they are all between 0 and 1***
    
    n: the number of terms of pouring back and forth
    Q: the amount we pour
    V: the volumn of both containers

Recursive formula:
    C_w1 = C_a2 = (Q * C_a1 + V * C_a2) / (Q+V)
"""


# we write a function based on the generalization
def concentration_of_water(C_w1,C_a1, C_w2,C_a2, Q, V, n):
    # we check for the invalid case
    if (C_w1 > 1 or C_w1 < 0) or (C_w2 > 1 or C_w2 < 0) or (C_a1 > 1 or C_a1 < 0) or (C_a2 > 1 or C_a2 < 0) or (n < 0):
        return "Invalid. Try again please."
    
    if n == 0:
        return C_w1;
    # when n >= 52, the difference between the concentration of water and alcohol
    # in both containers will almost be the same
    # that is, their difference will be smaller than 10 ** -12
    if n >= 54:
        return "You have reached the limit: the difference between the concetation of the water and alcohol in both containers will be smaller than 10 ** -12.\nWe can say that now they are 50% vs 50%."
    
    while (n > 0):
        
        C_w1 = (Q*C_a1+V*C_a2) / (V+Q)
        C_a2 = C_w1
        C_a1 = 1-C_w1
        C_w2 = C_a1
        n = n-1
    return C_w1

# test case:
test1 = concentration_of_water(1,0, 0,1, 50, 200, 1)
print(test1)

test2 = concentration_of_water(1,0, 0,1, 50, 200, 20)
print(test2)

test3 = concentration_of_water(1,0, 0,1, 50, 200, 55)
print(test3)
         
        
    
    