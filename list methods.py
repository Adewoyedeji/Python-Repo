s = [1, 3, 'm', 21, 'n', 5, 26, [3, 5, 7], [9, 25, 49], 35,  53, 'BH', 86, 'BELLA', 13, 'XANDER', 17, ]
t = ['PLATE', 742, 'MARKET', 50, 27, 41, 12, 'MILTON', [2,4], [6,8,11], 'LAND', [14, 'MILLION', 'NAIRA'], 14, 72, 36, 190,]
j = [1, 3, 2, 3, 4, 5, 3, 21, 1, 6, 7, 3, 15, 3, 33]
u = [1, 3, 5, 7, 9]
v = [2, 4, 6, 8, 10]
w = ['Dee', 'Jay', 'Bella', 'Xander']
z = ['Wole', 'Nike', 'Moji', 'Shade', 'Deji']

# s[i] = x (item i of s is replaced by x)

# EXAMPLE CODE:-
# print(s)
# s[3] = 12
# print(s)



# s[i:j] = t (slice of s from i to j is replaced by the contents of the iterable t)

# EXAMPLE CODE:-
# print(s)
# s[1:4] = 'Jay'
# print(s)




# del s[i:j](same as s[i:j] = [])

# EXAMPLE CODE:-
# print(s)
# del s[7:9]
# print(s)
# del s[4]
# print(s)




# s[i:j:k] = t (the elements of s[i:j:k] are replaced by those of t. ) t must have the same length as the slice it is
# replacing. The slice of s from i to j with step k is defined as the sequence of items with index x = i + n*k such
# that 0 <= n < (j-i)/k. In other words, the indices are i, i+k, i+2*k, i+3*k and so on, stopping when j is reached (
# but never including j). When k is positive, i and j are reduced to len(s) if they are greater. When k is negative,
# i and j are reduced to len(s) - 1 if they are greater. If i or j are omitted or None, they become “end” values (
# which end depends on the sign of k). Note, k cannot be zero. If k is None, it is treated like 1.

# EXAMPLE CODE:-
# print(s)
# print(u)
# print(s[1:16:3])
# s[1:16:3]= u
# print(s)




# s.index(x[, i[, j]])
# index of the first occurrence of x in s (at or after index i and before index j)

# EXAMPLE CODE:-
# print(s.index(35[2:15])). ???? check this code for correctness!!!!!!!



# s.count(x)
# total number of occurrences of x in s

# EXAMPLE CODE:-
# print(j)
# print(j.count(3))



# del s[i:j] = same as s[i:j] = []

# EXAMPLE CODE:-
# print(t)
# del t[1:12]
# print(t)


# s.append(x) :- appends x to the end of the sequence (same as s[len(s):len(s)] = [x])

# EXAMPLE CODE:-
# print(u)
# u.append(11)
# print(u)



# s.clear(). removes all items from s (same as del s[:])

# EXAMPLE CODE:-
# print(v)
# v.clear()
# print(v)



# s.copy(). creates a shallow copy of s (same as s[:])

# EXAMPLE CODE:-
# print(u)
# u.copy()
# print(u)



# s.extend(t) or s += t. extends s with the contents of t (for the most part the same as s[len(s):len(s)] = t)

# EXAMPLE CODE:-
# print(u)
# print(v)
# u.extend(v)
# print(u)



# s *= n. updates s with its contents repeated n times

# EXAMPLE CODE:-
# print(v)
# v *= 3
# print(v)



# s.insert(i, x). inserts x into s at the index given by i (same as s[i:i] = [x])

# EXAMPLE CODE:-
# print(w)
# w.insert(3, 'Missed Baby')
# print(w)




# s.pop([i]). retrieves the item at index i and also removes it from s
# The optional argument i defaults to -1, so that by default the last item is removed and returned.

# EXAMPLE CODE:-
# print(z)
# b = z.pop(4)
# print(z)
# print(b)




# s.remove(x). remove the first item from s where s[i] is equal to x.
# remove() raises ValueError when x is not found in s.

# EXAMPLE CODE:-
# print(j)
# j.remove(3)
# print(j)



# s.reverse(). reverses the items of s in place
# The reverse() method modifies the sequence in place for economy of space when reversing a large sequence.
# To remind users that it operates by side effect, it does not return the reversed sequence.

# EXAMPLE CODE:-
# print(w)
# w.reverse()
# print(w)

# line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# words = line.split()
# print(words)
