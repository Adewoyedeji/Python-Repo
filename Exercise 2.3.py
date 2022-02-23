
# Exercise 3: Write a program to prompt the user for hours and rate per
# hour to compute gross pay.
# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25


while True:
    hrs = input('Enter Hours: ')
    try:
        ihrs = float(hrs)
    except:
        print('Error. Enter Numbers not alphabet')
        continue
    if ihrs == float(hrs):
        break
while True:
    rate = input('Enter Rate: ')
    try:
        irate = float(rate)
    except:
        print('Error. Enter Number not alphabet')
        continue
    if irate == float(rate):
        break
pay = ihrs * irate
print(pay)