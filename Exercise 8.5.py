# Write a program to read through the mail box data and
# when you find line that starts with “From”, you will split the line into
# words using the split function. We are interested in who sent the
# message, which is the second word on the From line.
#
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
#
# You will parse the From line and print out the second word for each
# From line, then you will also count the number of From (not From:)
# lines and print out a count at the end. This is a good sample output
# with a few lines removed:
#
# python fromcount.py
# Enter a file name: mbox-short.txt
# stephen.marquard@uct.ac.za
# louis@media.berkeley.edu
# zqian@umich.edu
# [...some output removed...]
# ray@media.berkeley.edu
# cwen@iupui.edu
# cwen@iupui.edu
# cwen@iupui.edu
# There were 27 lines in the file with From as the first word

count = 0
file = input('Enter file name: ')
try:
    fhand = open(file)
except:
    print('File not found. Enter new file name')
    quit()
for line in fhand:
    words = line.split()
    #print(words)
    if len(words) == 0 or words[0] != 'From':
        continue
    count = count + 1
    print(words[1])
print ('There were', count, "lines in the file with 'From' as the first word")
