while True:
    hrs = input('Enter Hours: ')
    try:
        ihrs = float(hrs)
    except:
        print('Error, Please enter numeric input')
        continue
    if ihrs == float(hrs):
        break
while True:
    rate = input('Enter Rate: ')
    try:
        irate = float(rate)
    except:
        print('Error, Please enter numeric input')
        continue
    if irate == float(rate):
        break
def computepay(hrs, rate):
    if ihrs <= 40.0:
        pay = ihrs * irate
        return pay
    else:
        xhrs = ihrs - 40.0
        xrate = irate * 1.5
        xpay = xhrs * xrate
        npay = 40 * irate
        newpay = npay + xpay
        return newpay
print(computepay(hrs, rate))
