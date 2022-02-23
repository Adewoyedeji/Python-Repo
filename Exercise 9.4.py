# Write a program to read through a mail log, build a his-
# togram using a dictionary to count how many messages have come from
# each email address, and print the dictionary.
# Enter file name: mbox-short.txt
#
# RESULT:-
#
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
# 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
# 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
# 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
# 'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
# 'ray@media.berkeley.edu': 1}

# Add code to the above program to figure out who has the
# most messages in the file. After all the data has been read and the dic-
# tionary has been created, look through the dictionary using a maximum
# loop (see Chapter 5: Maximum and minimum loops) to find who has
# the most messages and print how many messages the person has.
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
    print('File not found. Enter a file name')
    quit()

for line in ofile:
    words = line.split()
    #print(words)
    if len(words) == 0 or words[0] != 'From' :
        continue
    #print(words)
    # if words[1] not in newdict:
    #     newdict[words[1]] = 1
    # else:
    #     newdict[words[1]] = newdict[words[1]] + 1
    newdict[words[1]] = newdict.get(words[1], 0) + 1

#print(newdict)

Mostmail = None
Mostcount = None

for mail, count in newdict.items():
    if Mostcount is None or count > Mostcount:
        Mostmail = mail
        Mostcount = count



print(Mostmail,Mostcount)