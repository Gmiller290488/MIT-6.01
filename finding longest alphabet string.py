# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 10:58:46 2016

@author: dell
"""

s = 'egbsdrcymqdgpfkeipcsqv'

newChar = ""
newWord = ""
temp_length = 0
max_string = 0
output = ""
for i in range(0,len(s)):
    if s[i] >= newChar:
        newWord += s[i]
        
        newChar = s[i]
        if len(newWord) > len(output):
            output = newWord
    else:
        
        newWord = s[i]
        newChar = s[i]

print("Longest substring in alphabetical order is: " + output)

    
        
    
    