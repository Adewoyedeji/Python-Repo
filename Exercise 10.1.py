# Revise a previous program as follows: Read and parse the
# “From” lines and pull out the addresses from the line. Count the num-
# ber of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits
# by creating a list of (count, email) tuples from the dictionary. Then
# sort the list in reverse order and print out the person who has the most
# commits.
#
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
#
# RESULT:-
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# Enter a file name: mbox.txt
# zqian@umich.edu 195


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
    newdict[words[1]] = newdict.get(words[1], 0) + 1


#                  OR
# for line in ofile:
#     words = line . split()
#     if len(words) == 0 or words[0] != 'From' :
#         continue
#     for word in words:
#         addy = words[1]
#     newdict[addy] = newdict.get(addy, 0) +1


#                   OR
# for line in ofile:
#     words = line . split()
#     if len(words) == 0 or words[0] != 'From' :
#         continue
#     for word in words:
#         addy = words[1]
#     if addy not in newdict:
#         newdict[addy] = 1
#     else:
#         newdict[addy] = newdict[addy] + 1

#print (newdict)
newlist = list()

for key, value in list(newdict.items()):
    newlist.append((value, key))

newlist.sort(reverse=True)
#print(newlist)

for value,key in newlist[:1]:
    print(key,value)