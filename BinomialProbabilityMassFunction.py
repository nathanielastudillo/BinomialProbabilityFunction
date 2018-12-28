#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 18:40:07 2018

@author: nathanielastudillo
"""

'''
Binomial Probability Mass Function
'''

import math as m

def binomialPmass(x,n,p):
    '''
    x = number of successes
    n = number of trials 
    p = probability of trial
    '''
    
    combination = (m.factorial(n)/(m.factorial(x)*m.factorial(n-x)))
    pToTheX = p**x

    return combination * pToTheX * ((1-p)**(n-x))
    