from typing import TextIO

newdict = dict()
newlist1 = list()

file = input(' Enter file name: ')

try:
    fhand = open(file, encoding="utf8")  # the (encoding="utf8") part was added because i kept getting error codes
except:                                  # about the encoding. searched on stack overflow and found how to force
    print('File not found')              # it to use utf8 encoding
    quit()

for line in fhand:
    line = line.strip()
    newline = line[16:]
    #print(newline)
    if newline.startswith('+234 802 474 1100'):
        print(newline)
    elif newline.startswith('+234 803 075 0650'):
        print(newline)
    else:
        continue
    #words = newline.split(':')
    #print(words)
    # for word in words:
    #     name = words[0]
    #     print(name)