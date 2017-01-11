# -*- coding: utf-8 -*-
balance = 5000
annualInterestRate = 0.18
monthlyPaymentRate = 0.02
month = 0
totalPaid = 0
for month in range(12):
    payment = balance * monthlyPaymentRate
    totalPaid += payment
    balance = balance - payment
    interestAdded = balance * (annualInterestRate/12)
    balance = balance + interestAdded
    print("Month ", round(month, 2))
    print("Minimum payment is £", round(payment, 2))
    print("Remaining balance is £", round(balance, 2))
    month += 1

print("Total amount paid £", round(totalPaid, 2))
print("Remaining balance £", round(balance, 2))

    

    
