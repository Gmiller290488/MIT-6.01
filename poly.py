# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 10:24:43 2016

@author: dell
"""

#def general_poly(L):
#    """ L, a list of numbers (n0, n1, n2, ... nk)
#    Returns a function, which when applied to a value x, returns the value 
#    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
#    def result(x):    
#        n, tmp = 0, 0
#        for a in L:
#            tmp = tmp + (a * (x**n))
#            n += 1
#        return tmp
#    return result
#    
# Paste your code here
def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def result(x):
        pos = len(L)-1
        tmp = 0
        for num in L:
            tmp = tmp + (num * (x**pos))
            pos -=1
        return tmp
    return result
        


