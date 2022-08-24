
counts = dict()
file = input('Enter file name:')

try:
    fhand = open(file)
except:
    print('file not found. Enter file name. ')
    quit()

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1 # This line creates the dictionary
#print(counts)

newlist = list()
for k,v in counts.items():                         # This line runs through the dictionary in Key(k), value(v) pairs.
    newtuple = (v, k)                              # This line reverses the key value pair to value key pair
    newlist.append(newtuple)                       # This line appends the new value key pair to newlist
# #print(newlist)
 
newlist = sorted (newlist, reverse = True)         # This line sorts the value key pair.
                                                   # The "reverse = True" sorts it from highest to lowest.
print(newlist)

for v, k in newlist:
    print(k, v)                                    # This line reverses the value key pair back to key value pair

for v, k in newlist[ :10]:                         # This line only considers the first 10 value key pairs.
    print(k, v)

                                                   # Line 17 to 25 can be written in one land of code as below

print( sorted ([(v, k) for k, v in counts.items()]))
