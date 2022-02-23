# Welcome ADEWOYE AYODEJI ADESHOLA from Using Python to Access Web Data
#
# Finding Numbers in a Haystack
#
# In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.
#
# Data Files
# We provide two files for this assignment.
# One is a sample file where we give you the sum for your testing
# and the other is the actual data you need to process for the assignment.
#
# Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
# Actual data: http://py4e-data.dr-chuck.net/regex_sum_867377.txt (There are 91 values and the sum ends with 173)
#
# These links open in a new window.
# Make sure to save the file into the same folder as you will be writing your Python program.
# Note: Each student will have a distinct data file for the assignment -
# so only use your own data file for analysis.
#
# The sum for the sample text above is 27486.
# The numbers can appear anywhere in the line.
# There can be any number of numbers in each line (including none).
#
# Handling The Data
# The basic outline of this problem is to read the file,
# look for integers using the re.findall(),
# looking for a regular expression of '[0-9]+'
# and then converting the extracted strings to integers and summing up the integers.

import re
sum = 0
file = input('Enter file name: ')

try:
    ofile = open(file)
except:
    print('File name not found. Enter file name')
    quit()

for line in ofile:
    line = line.rstrip()
    x = re.findall('([0-9]+)', line)
    if len(x) <= 0:
        continue
    #print(x)
    for num in x:
        inum = int(num)
        sum = sum + inum
print(sum)