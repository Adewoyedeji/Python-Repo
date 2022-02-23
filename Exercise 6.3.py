# Encapsulate this code

# word = 'banana'
# counter = 0
# for letter in word:
#    if letter == 'a':
#        counter = counter + 1
# print(counter)

# in a function named count, and
# generalize it so that it accepts the string and the letter as arguments.

word = 'banana'
def count(word, index):
    counter = 0
    for letter in word:
        if letter == index:
            counter = counter + 1
    return counter
num = (count(word, 'n'))
print(num)
