# Write a program that records the domain name (instead of the
# address) where the message was sent from instead of who the mail came
# from (i.e., the whole email address). At the end of the program, print
# out the contents of your dictionary.
# python schoolcount.py
#
# RESULT :-
#
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}


#                                         CODE 1

newdict = dict()
newlist = list()

# file = input('Enter file name: ')
#
# try:
#     ofile = open(file)
# except:
#     print('File name not found. Please enter file name')
#
# for line in ofile:
#     words = line. split()
#     #print(words)
#     if len(words) == 0 or words[0] != 'From':
#         continue
#     #print(words)
#     #print(words[1])
#     newlist.append(words[1])
# #print(newlist)
# for mail in newlist:
#     pos = mail.find('@')
#     domain = mail[pos + 1: ]
#     #print(domain)
#     newdict[domain] = newdict.get(domain, 0) + 1
# print(newdict)

#                                      OR

file = input('Enter file name: ')
try:
    ofile = open(file)
except:
    print('File name not found. Please enter file name')
    quit()

for line in ofile:
    words = line. split()
    #print(words)
    if len(words) == 0 or words[0] != 'From':
        continue
    #print(words)
    email = words[1]
    #print(email)
    pos = email.find('@')
    domain = email[pos + 1:]
    #print(domain)
    newdict[domain] = newdict.get(domain, 0) + 1
print(newdict)




