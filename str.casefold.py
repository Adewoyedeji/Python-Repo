# str.casefold()
#Return a casefolded copy of the string. Casefolded strings may be used for caseless matching.

#Casefolding is similar to lowercasing but more aggressive
#because it is intended to remove all case distinctions in a string.
#For example, the German lowercase letter 'ß' is equivalent to "ss".
#Since it is already lowercase, lower() would do nothing to 'ß'; casefold() converts it to "ss".

word = 'bootylicioushoneypie'
word2 = 'BOOTYLICIOUSHONEYPIE'
x = word.casefold()
y = word2.casefold()
print(x)
print(y)