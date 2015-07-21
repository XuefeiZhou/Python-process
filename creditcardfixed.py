balance = 320000 #信用卡欠款
annualInterestRate = 0.2 #银行年利率
#以上数据会由系统提供，在这里只是为了测试

monthly_interest_rate = annualInterestRate / 12.0
minimumpay = balance / 12.0
maximumpay = (balance * (1 + monthly_interest_rate)**12) / 12.0


def totalinterest(monthpay):
    month = 1
    mybalance = balance
    totalinterest = 0
    while month < 13:
        mybalance = mybalance - monthpay
        interest = mybalance * monthly_interest_rate
        mybalance = mybalance + interest
        if mybalance <= 0:
            break
        else:
            totalinterest += interest
            month += 1
    return round(totalinterest,2)

monthpay = round((minimumpay + maximumpay) /2.0,2)
while monthpay <= balance:
    if 12 * monthpay - balance - totalinterest(monthpay) < -0.1:
        minimumpay = monthpay
        monthpay = round((minimumpay + maximumpay) /2.0,2)
    elif 12 * monthpay - balance - totalinterest(monthpay)> 0.1:
        maximumpay = monthpay
        monthpay = round((minimumpay + maximumpay) /2.0,2)
    else:
        break
print "Lowest Payment: ", monthpay







