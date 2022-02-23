# Write a while loop that starts at the last character in the
# string and works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.

fruit = 'banana'
x = 1
y = len(fruit)
while x <= y:
    z = fruit[y-x]
    print(z)
    x = x + 1

#Another way o construct same program is
#lfruit = len(fruit)
#while lfruit >=1:
    #letter = fruit [lfruit -1]
    #print (letter)
    #lfruit = lfruit - 1