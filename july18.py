#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 11:54:10 2022

@author: zhangkexin
"""

"""
Jul 18: Brainteaser 
Extention
---------
Can we generalize the at least socks problem?

We define:
    pairs: the number of pairs of socks at least to get
    socks: a list consisting of the number of different color socks
    takeout: the answer

formula: 
    takeout = (number of colors whose amounts are smaller than the number of pairs)+
              number of remaining colors*(pairs*2-1)+1
               
""" 

def socks(pairs,socks):
    # check invalid cases
    if len(socks) < 1 or pairs < 0:
        return "Invalid input, try again please"
    takeout = 0
    remaining = len(socks)
    
    # count the colors whose amounts are smaller than the number of pairs
    for i in socks:
        if i < 2*pairs:
            takeout += i
            remaining -=1
    
    takeout += remaining*(2*pairs-1)+1
    return takeout

# test case:
print('The number we must take out to guarantee at least 1 pair of socks with the same color is:')
print(socks(1,[8,11]))
print()
print('The number we must take out to guarantee at least 3 pairs of socks with the same color is:')
print(socks(3,[2,4,6,8,10,12,14,16,18,20]))
    
    
    
        
    