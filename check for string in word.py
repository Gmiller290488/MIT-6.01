# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 07:35:02 2016

@author: Gareth
"""
s = 'bobobobilllibob'
count = 0
i = 0
for char in s:
    if i+2 < len(s):    
        if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
            count += 1
            
    i += 1
print("Number of times bob occurs is: ", count)
