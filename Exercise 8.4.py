# Download a copy of the file www.py4e.com/code3/romeo.txt.
# Write a program to open the file romeo.txt and read it line by line. For
# each line, split the line into a list of words using the split function.
# For each word, check to see if the word is already in a list. If the word
# is not in the list, add it to the list. When the program completes, sort
# and print the resulting words in alphabetical order.

# ANSWER:-
# Enter file: romeo.txt
# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
# 'and', 'breaks', 'east', 'envious', 'fair', 'grief',
# 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
# 'sun', 'the', 'through', 'what', 'window',
# 'with', 'yonder'] 



newlist = list()
file = input('Enter file name: ')
try:
    fhand = open(file)
except:
    print('Error: File not found. Enter new file')
    quit()
for line in fhand:
    words = line.split()
    print(words)
    for word in words:
        if word not in newlist:
            newlist.append(word)
newlist.sort()
print(newlist)
