#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 13:01:55 2022

@author: zhangkexin
"""

"""
Jul 9: Brainteaser 
Extention
---------
Can we generalize the bell rings problem?

1. first, we need a greatest common divider function and a least common mutiples.
define:
    A: the smaller number
    B: the bigger number
    
    logic: 
    1. GCD:
    B = A*p + q
    // q: B - multiples of A
    // since g is the greatest common divider of A and B
    // A, B themselves are the multiples of g
    // B = x * g, A = y * g
    // regardless of what x,y are, the difference betwen A and B will be
    // (x-y)*g
    // q is the value when x = 1 but y != 1
    // q is also a multiple of g
    
    2. LCM:
    least common multiples * greatest common divider = A*B
    


"""

def gcd(A,B):
    if A == 0:
        return B
    return gcd(B%A,A)

def lcm(a,b):
    return a*b / gcd(a,b)


"""
2. Next, if we want to generalize the bell rings, we define in this way:
    bells: a list consisting of the velocities of bells ringing. unnit: times per minute
    ans: the next time they ring at the same timein minutes
    
"""
def bellrings(bells):
    if (len(bells) < 2):
        return "Try again."
    intervals = []
    for i in range(len(bells)):
        intervals.append(60 / bells[i])
        
    # we sort it for calculation
    intervals = sorted(intervals)
        
    # we find the largest common divider of the intervals

    ans = lcm(intervals[0],intervals[1]);
    
    
    for i in range(2,len(intervals)):
        ans = lcm(ans,intervals[i])
    return ans / 60

# test cases
print(bellrings([]))
print(bellrings([1]))
print(bellrings([5,4]))
print(bellrings([3,60/25,2]))
print(bellrings([1/45,1/30,1/36]))

    