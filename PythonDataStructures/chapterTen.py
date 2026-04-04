# Tuples

"""
Tuples are like Lists
Tuples are another kind of sequence that functions much like a list
- they have elements which are indexed starting at 0
"""
x = ('Glenn', 'Sally', 'Joseph')
print(x[2])
y = (1, 9, 2)
print(max(y))

"""
but... Tuples are "immutable"
Unlike a list, once you create a tuple, you cannot alter its contents - similar to a string
"""
z = (5, 4, 3)
#z[2] = 0
# Traceback:...

"""
Tuples Are More Efficient
- Since Python does not have to build tuple structures to be modifiable, they are similer and more efficient in term of memory use and performance than lists
- So in our program when we are making "temporary variables" we prefer tuples over lists
"""

# Tuples and Assignement
"""
- We can also put a tuple on the left-hand side of an assignement statement
- We can even omit the parentheses
"""
(x, y) = (4, 'fred')
print(y)

#Tuples and Dictionaries
"""
The items() method in dictionaries returns a list of (key, value) tuples
"""
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print(k, v)

tups = d.items()
print(tups)

# Tuples are Comperable
"""
The comparision operators work with tuples and other sequences. If the first item is equal, Python goes on the next element, and so on,
until finds elements that differ.
"""
print ((0, 1, 2) < (5, 1, 2))
print ((0, 1, 20000000) < (0, 3, 4))
print(('Jones', 'Sally') < ('Jones', 'Sam'))

# Sorting Lists of Tuples
"""
- We can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary
- First we sort the dictionary by the key using the items() method and sorted() function
"""
d = {'a':10, 'c':20, 'b':1}
print(d.items())
print(sorted(d.items()))

# Using sorted()
"""
We can do this even more directly using the built-in function sorted
that takes a sequence as a parameter and returns a sorted sequence
"""
d = {'b':1, 'c':22, 'a':10}
t = sorted(d.items())
print(t)
for k, v in sorted(d.items()):
    print(k, v)

# Sort by Values Instead of Key
"""
- If we could construct a list of tuples of the form (value, key) we could sort by value
- We do this with a for loop that creates a list of tuples
"""
c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k,v in c.items():
    tmp.append((v,k))
print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)

#even shorter version
"""
List comprehension create a dynamic list. In this case, we make a list of reversed tuples and then sort it.
"""
print(sorted([ (v, k) for k,v in c.items() ]))

x, y = 3, 4
print(y)