# Write a program to read through a file and print the contents
# of the file (line by line) all in upper case.

fname = input('Enter file name: ')
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    fupp = line.upper()
    print (fupp)
    #print ("Original line: ", line)