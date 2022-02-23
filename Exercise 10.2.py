# This program counts the distribution of the hour of the day
# for each of the messages. You can pull the hour from the “From” line
# by finding the time string and then splitting that string into parts using
# the colon character. Once you have accumulated the counts for each
# hour, print out the counts, one per line, sorted by hour as shown below.
# python time of day.py
#
# RESULT:-
# Enter a file name: mbox-short.txt
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

newdict = dict()
file = input('Enter file name: ')

try:
    ofile = open(file)
except:
    print('File cannot be found. Enter file name')
    quit()

for line in ofile:
    words = line.split()
    if len(words) == 0 or words[0] != 'From' :
        continue
    #print(words)
    time = words[5]
    slice = time.split(':')
    #print(slice)
    newdict[slice[0]] = newdict.get(slice[0], 0) + 1

#print(newdict)

newlist = list()
for key, value in list(newdict.items()):
    newlist.append((key, value))
newlist.sort()

for key, value in newlist:
    print(key, value)

#                 OR
#
# newlist = list(newdict.items())
# newlist.sort()
# #OR
# #newlist = list(sorted(newdict.items()))
# for key, val in newlist:
#     print(key, val)
