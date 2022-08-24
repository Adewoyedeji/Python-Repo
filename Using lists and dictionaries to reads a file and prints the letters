# Write a program that reads a file and prints the letters
# in decreasing order of frequency. Your program should convert all the
# input to lower case and only count the letters a-z. Your program should
# not count spaces, digits, punctuation, or anything other than the letters
# a-z.

letters = list()
newdict = dict()

file = input('Enter file name: ')
try:
    ofile = open(file)
except:
    print('File name not found. Enter file name')
    quit()

for line in ofile:
    if len(line) < 1:
        continue
    # print(line)
    line = line.lower()
    line = line.rstrip()
    #print(line)
    for i in line:
        if i.isalpha() == True:
            letters.append(i)
#print(letters)

for letter in letters:
    newdict[letter] = newdict.get(letter, 0) + 1

#print(newdict)

newlist = list()

for k,v in list(newdict.items()):
    newlist.append((v,k))
#print(newlist)
newlist.sort(reverse=True)
#print(newlist)
for v,k in newlist:
    print(k,v)
