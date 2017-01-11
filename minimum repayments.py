balance = 320000
annualInterestRate = 0.2
month = 0
endBalance = balance
minPayment = 10
while (endBalance/12 - minPayment) > 0:
    for month in range(13):
        endBalance -= minPayment
        endBalance = endBalance + (endBalance*(annualInterestRate/12))
        month += 1
    endBalance = balance
    minPayment += 10
    
print(minPayment)
print(endBalance)