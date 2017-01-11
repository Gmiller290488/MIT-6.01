from math import *

def polysum(n, s):
    '''Function takes two numbers, and uses them to find the area and square perimeter of a regular
    polygon, to 4 decimal places'''
    area = ((0.25*n*(s**2))/tan(pi/n))
    perimeter = (n*s)**2
   
    sum = area + perimeter
    return round(sum, 4)

polysum(6, 4.5)