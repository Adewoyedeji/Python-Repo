word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)


# The result is {'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}

# Dictionaries have a method called get that takes a key and a default value. If the
# key appears in the dictionary, get returns the corresponding value; otherwise it
# returns the default value.
#
# For example:
#
# >>> counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# >>> print(counts.get('jan', 0))
# 100
# >>> print(counts.get('tim', 0))
# 0
#
# We can use get to write our histogram loop more concisely. Because the get
# method automatically handles the case where a key is not in a dictionary, we can
# reduce four lines down to one and eliminate the if statement.


word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c, 0) + 1
print(d)


# This is the result :- {'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}.
# This is same as using the first code