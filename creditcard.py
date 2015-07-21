balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthly_interest_rate = float(annualInterestRate) / 12.0
mybalance = float(balance)
totalpayment = 0
for month in range(1,13):
    payment = round(mybalance * monthlyPaymentRate,2)
    myrest = round(mybalance - payment,2)
    interest = round(myrest * monthly_interest_rate,2)
    mybalance = round(mybalance + interest - payment,2)
    totalpayment += payment
    print "Month: ",month
    print "Minimum monthly payment: ",payment
    print "Remaining balance: ",mybalance
print "Total paid: ",totalpayment
print "Remaining balance: ", mybalance
