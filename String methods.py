word = 'bootylicioushoneypie'
word2 = 'BOOTYLICIOUSHONEYPIE'
word3 = 'booty\tlicious\thoneypie'
word4 = 'life is hard'
word5 = 'lif3ish7rd'
word6 = 'lif3 is h7rd'
word7 = '332356598'
word8 = '332 456 321 222'
word9 = '13579'
word10 = '2468'



# str.capitalize()
# Return a copy of the string with its first character capitalized
# and the rest lowercased.

# x = word.capitalize()
# print(x)

# RESULT :-
#
# Bootylicioushoneypie






# str.casefold()
# Return a casefolded (lowering the case) copy of the string.
# Casefolded strings may be used for caseless matching.
#
# Casefolding is similar to lowercasing but more aggressive
# because it is intended to remove all case distinctions in a string.
# For example, the German lowercase letter 'ß' is equivalent to "ss".
# Since it is already lowercase, lower() would do nothing to 'ß';
# casefold() converts it to "ss".

# x = word.casefold()
# y = word2.casefold()
# print(x)
# print(y)
#
# RESULT:-
#
# bootylicioushoneypie
# bootylicioushoneypie





# str.center(width[, fillchar])
# Return centered in a string of length width.
# Padding is done using the specified fillchar (default is an ASCII space).
# The original string is returned if width is less than or equal to len(s)

# print(len(word)) # word has len = 20

# u = word.center(5)
# v = word.center(10)
# w = word.center(15)
# x = word.center(20)
# y = word.center(25)
# z = word.center(30)
# a = word.center(35)
# b = word.center(40)
#
# print(u)
# print(v)
# print(w)
# print(x)
# print(y)
# print(z)
# print(a)
# print(b)
#
# RESULT:-
#
# bootylicioushoneypie
# bootylicioushoneypie
# bootylicioushoneypie
# bootylicioushoneypie
#    bootylicioushoneypie
#      bootylicioushoneypie
#         bootylicioushoneypie
#           bootylicioushoneypie







# str.count(sub, start, end)
# Return the number of non-overlapping occurrences of substring sub in the range [start, end].
# Optional arguments start and end are interpreted as in slice notation.

# x = word.count('o')
# y = word.count('o', 0, 6) # means count 'o's from 0th letter to the 6th letter
# print(x)
# print(y)
#
# RESULT:-
# 4
# 2





# str.encode(encoding="utf-8", errors="strict")
# Return an encoded version of the string as a bytes object.
# Default encoding is 'utf-8'.
# errors may be given to set a different error handling scheme.
# The default for errors is 'strict', meaning that encoding errors raise a UnicodeError.
# Other possible values are 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace'
# and any other name registered via codecs.register_error(), see section Error Handlers.
# For a list of possible encodings, see section Standard Encodings.

# x = word.encode()
# print(x)
#
# RESULT:-
#
# b'bootylicioushoneypie'







# str.expandtabs(tabsize=8)
# Return a copy of the string where all tab characters are replaced by one or more spaces,
# depending on the current column and the given tab size.
# Tab positions occur every tabsize characters
# (default is 8, giving tab positions at columns 0, 8, 16 and so on).
# To expand the string, the current column is set to zero and the string is examined character by character.
# If the character is a tab (\t), one or more space characters are inserted in the result
# until the current column is equal to the next tab position.
# (The tab character itself is not copied.)
# If the character is a newline (\n) or return (\r),
# it is copied and the current column is reset to zero.
# Any other character is copied unchanged
# and the current column is incremented by one regardless of how the character is represented when printed.

# x = word3.expandtabs()
# print(x)
#
# RESULT :-
# booty   licious honeypie






# str.find(sub[, start[, end]])
# Return the lowest index in the string where substring sub is found
# within the slice s[start:end].
# Optional arguments start and end are interpreted as in slice notation.
# Return -1 if sub is not found.

# x = word.find('y')
# y = word.find('y', 5, 10)
# z = word.find('y', 10, 20)
# a = word.find('y', 0, 20)
#
# print(x, y, z, a)
#
# RESULT:-
#
# 4 -1 16 4





# str.index(sub[, start[, end]])
# Like find(), but raise ValueError when the substring is not found.

# x = word.index('u')
# # y = word.index('u', 0, 5) This line gives value error
# z = word.index('u', 7, 20)
#
# print(x)
# #print(y) this print gives value error
# print(z)
#
# RESULT:-
#
# 10
# 10





# str.isalnum()
# Return True if all characters in the string are alphanumeric
# and there is at least one character, False otherwise.
# A character c is alphanumeric if one of the following returns True:
# c.isalpha(), c.isdecimal(), c.isdigit(), or c.isnumeric().

# word = 'bootylicioushoneypie'
# word4 = 'life is hard'
# word5 = 'lif3ish7rd'
# word6 = 'lif3 is h7rd'
# word7 = '332356598'
# word8 = '332 456 321 222'
# print(word.isalnum())
# print(word4.isalnum())
# print(word5.isalnum())
# print(word6.isalnum())
# print(word7.isalnum())
# print(word8.isalnum())
#
# RESULT:-
#
# True
# False         # word4 contains white spaces.
# True
# False         # word6 contains white spaces
# True
# False         # word 8 contains white spaces

# Same logic works for the following:-
#
# 1. word.isalpha():-
# Return True if all characters in the string are alphabetic
# and there is at least one character, False otherwise.
# Alphabetic characters are those characters
# defined in the Unicode character database as “Letter”,
# i.e., those with general category property being one of
# “Lm”, “Lt”, “Lu”, “Ll”, or “Lo”.
# Note that this is different from the “Alphabetic” property
# defined in the Unicode Standard.
#
#
# 2. word.isdecimal()
# Return True if all characters in the string are decimal characters
# and there is at least one character, False otherwise.
# Decimal characters are those that can be used to form numbers in base 10,
#
#
# 3. word.isdigit()
# Return True if all characters in the string are digits
# and there is at least one character, False otherwise.
# Digits include decimal characters and digits that need special handling,
# such as the compatibility superscript digits.
# This covers digits which cannot be used to form numbers in base 10,
# like the Kharosthi numbers. Formally, a digit is a character
# that has the property value Numeric_Type=Digit or Numeric_Type=Decimal.


# 4. str.islower()
# Return True if all cased characters in the string are lowercase
# and there is at least one cased character, False otherwise.
#
#
# 5. str.isnumeric()
# Return True if all characters in the string are numeric characters,
# and there is at least one character, False otherwise.
# Numeric characters include digit characters,
# and all characters that have the Unicode numeric value property,
# e.g. U+2155, VULGAR FRACTION ONE FIFTH.
# Formally, numeric characters are those with the property value
# Numeric_Type=Digit, Numeric_Type=Decimal or Numeric_Type=Numeric.
#
#
# 6. str.isspace()
# Return True if there are only whitespace characters in the string
# and there is at least one character, False otherwise.
# A character is whitespace if in the Unicode character database (see unicodedata),
# either its general category is Zs (“Separator, space”),
# or its bidirectional class is one of WS, B, or S.


# 7. str.istitle()
# Return True if the string is a titlecased string and
# there is at least one character,
# for example uppercase characters may only follow uncased characters
# and lowercase characters only cased ones. Return False otherwise.
#
#
# 8. str.isupper()
# Return True if all cased characters in the string are uppercase
# and there is at least one cased character, False otherwise.






# str.join(iterable)
# Return a string which is the concatenation of the strings in iterable.
# A TypeError will be raised if there are any non-string values in iterable,
# including bytes objects. The separator between elements is the string providing this method.

# word9 = '13579'
# word10 = '2468'
# x = word9.join(word10)
# y = word10.join(word9)
# print(x)
# print(y)
#
# RESULT:-
#
# 2135794135796135798.          # This is 2(13579),4(13579),6(13579),8(13579)
# 124683246852468724689         # This is 1(2468), 3(2468), 5(2468),7(2468), 9(2468)