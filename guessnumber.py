# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 18:52:50 2016

@author: dell
"""

# guess the users number game

#set variables: guess, lowNo, highNo. 
lowNo = 0
highNo = 100
answer = ' '
print("Please think of a number between 0 and 100!")
while answer != 'c' or 'h' or 'l':
    guess = (highNo + lowNo) // 2
    print("Is your secret number ", (guess),end='')
    print("?")
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")    
    if answer == 'c':
        print("Game over. Your secret number was: ", guess)
        break
    elif answer == 'h':
        highNo = guess
    elif answer == 'l':
        lowNo = guess
    else:
        print("Sorry, I did not understand your input.")
        

       
        
        
