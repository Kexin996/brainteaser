#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 15:33:48 2022

@author: zhangkexin
"""

"""
Jul 9: Brainteaser 
Extention
---------
Can we generalize the escalator problem?

We define:
    D_m: the steps Mayon has reached
    D_f: the steps Fischer has reached
    ratio: the velocity ratio of Mayon vs. Fischer
    e.g. ratio = 3/2 ---> V_m / V_f
    
Formula:
    D_total = D_f + (D_m-D_f)*D_f / ((D_f - D_m/ ratio))

"""

def total_distance(D_m, D_f, ratio):
    return D_f + (D_m-D_f)*D_f / ((D_f - D_m/ ratio))

# testcase:
print(total_distance(25, 20, 3/2));
    