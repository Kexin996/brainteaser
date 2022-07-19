#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 11:04:50 2022

@author: zhangkexin
"""

"""
Jul 19: Brainteaser 
Extention
---------
Can we generalize the simple guessing number problem?

We define:
    N: the winning number
    players: the ntotal umber of players
    interval: the maximum interval between two guessing numbers
    //        e.g. interval = 10 ---> b = [a+1,a+10]
    stategy: a list consisting of successful moves
    
We assume that we are any of the play who finally gets N

formula:
    x(n) = x(n+1) - (the interval of y*numberOfOtherPlayers+1)
    n: the number of turns
    note: we work backward
""" 

def winning(N,players,interval):
    if interval == 0 or players <= 1:
        return "Invalid, try again please."
    strategy = [N]
    x = N
    while x > 1:
        x -= (interval*(players-1)+1)
        if x > 1:
            strategy.append(x)
    if x == 1:
        # that means we must be the first player in order to win
        strategy.append(x)
        print("Hey, We must be the first one to win")
    else:
        print("Who is the first to play will win the game.")
    return strategy

# testcase
print(winning(50,2,10))
print("\n")
print(winning(100,2,10))
print("\n")
print(winning(50,3,10))
print("\n")
        
        
        
        
    
   
    
    
