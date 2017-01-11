# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 08:32:13 2016

@author: dell
"""

trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
          
def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    answer = ""
    if int(us_num) <= 10:
        return trans[us_num]
    elif int(us_num) > 10 and int(us_num) < 20:
        tens = (int(us_num)// 10) * 10
        digits = int(us_num) % 10
        answer += trans[str(tens)]
        answer += " "
        answer += trans[str(digits)]
        return answer
    elif int(us_num) >= 20 and int(us_num) < 100:
        tens = (int(us_num)// 10) 
        digits = int(us_num) % 10        
        if int(us_num) % 10 == 0:
            answer += trans[str(tens)]
            answer += " "
            answer += trans["10"]
        else:
            answer += trans[str(tens)]
            answer += " "
            answer += trans['10']
            answer += " "
            answer += trans[str(digits)]
        return answer

print(convert_to_mandarin("30"))
        
        

