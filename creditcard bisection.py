# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 18:58:24 2016
minimum credit card repayments to the pence
using bisection search
@author: Gmiller
"""
monthlyInterestRate = annualInterestRate/12.0
lowerPayment = balance/12.0
upperPayment = ((balance*(1 + monthlyInterestRate)**12)/12.00)
newBalance = balance
while newBalance != 0:
    guess = (upperPayment + lowerPayment) / 2
    newBalance = balance
    for month in range(12):
        newBalance -= guess
        newBalance = newBalance + (newBalance*monthlyInterestRate)
    if round(newBalance, 0) == 0:
        break
    elif newBalance > 0:
        lowerPayment = guess
    elif newBalance < 0:
        upperPayment = guess
        
print("Lowest Payment: ", round(guess, 2))