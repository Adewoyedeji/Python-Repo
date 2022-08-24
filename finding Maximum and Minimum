# Write another program that prompts for a list of numbers
# as above and at the end prints out both the maximum and minimum of
# the numbers instead of the average.

maximum = None
minimum = None
count = 0
while True:
    num = input('Enter number: ')
    if num == "done":
        break
    try:
        inum = float(num)
    except:
        print("Error, Enter a number")
        continue
    count = count + 1
    if maximum is None:
        maximum = inum
    elif inum > maximum:
        maximum = inum
    if minimum is None:
        minimum = inum
    elif inum < minimum:
        minimum = inum
print (count, maximum, minimum)
