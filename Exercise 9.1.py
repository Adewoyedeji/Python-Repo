# Download a copy of the file www.py4e.com/code3/words.txt
# Write a program that reads the words in words.txt and stores them as
# keys in a dictionary. It doesn’t matter what the values are. Then you
# can use the in operator as a fast way to check whether a string is in the
# dictionary.

newdict = dict()
n = 1
file = input('Enter file name: ')

try:
    fhand = open(file)
except:
    print('File name not found. Enter another file name')

for line in fhand:
    words = line.split()
    if len(words) == 0:
        continue
    #print(words)
    for word in words:
        newdict[word] = n
        n = n + 1
#print(newdict)
