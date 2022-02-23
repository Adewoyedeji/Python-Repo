# Exercise 3: Write a program to prompt the user for hours and rate per
# hour to compute gross pay.Write your pay computation to give the employee 1.5
# times the hourly rate for hours worked above 40 hours.
# Make your program handle non-numeric input gracefully by printing an error message
# and exiting the program.
# 1) Enter Hours: 35      (2)  Enter Hours: 45
#    Enter Rate: 2.75          Enter Rate: 10
#    Pay: 96.25                Pay: 475.0


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
if ihrs <= 40.0:
    pay = ihrs * irate
    print(pay)
else:
    xhrs = ihrs - 40.0
    xrate = irate * 1.5
    xpay = xhrs * xrate
    npay = 40 * irate
    newpay = npay + xpay
    #print(xpay)
    #print(npay)
    print(newpay)