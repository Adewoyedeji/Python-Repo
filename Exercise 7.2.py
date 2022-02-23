# Write a program to prompt for a file name, and then read
# through the file and look for lines of the form:
#
# X-DSPAM-Confidence: 0.8475#
# When you encounter a line that starts with “X-DSPAM-Confidence:”
# pull apart the line to extract the floating-point number on the line.
# Count these lines and then compute the total of the spam confidence
# values from these lines. When you reach the end of the file, print out
# the average spam confidence.

fname = input('Enter file name: ')
fhand = open(fname)
count = 0
sum = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        #print(line)
        pos = line.find(':')
        slice = line[pos+1:]
        fslice = float(slice)
        #print(fslice)
        count = count + 1
        sum = sum + fslice
print(count, sum/count)