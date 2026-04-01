# Dictionaries

## What is a Collection?
"""
- A collection is nice because we can put more than one value in it and carry them all in one convinient package
- We have a bunch of values in a single "variable"
- We do this by having more than one place "in" the variable
- We have ways of finding the different places in the variable
"""
## What is Not A "Collection"?
"""
Most of our variables have one value in them - when we put a new value in the variable - the old value is overwritten
"""
## A Story of Two Collections ..
"""
- List
A linear collection of values Lookup by position 0 .. lenght-1
- Dictionary
A linear collection of key-value pairs Lookup by "tag" or "key"
"""
## Dictionaries
"""
- Dictionaries are Python's most powerfull data collection
- Dictionaries allow us to do fast database-like operations in Python
- Similar concepts in different programming languages
    - Associative Arrays - Perl/PHP
    - Properties of Map or HashMap - Java
    - Property Bag - C#/.Net
"""
## Dictionaries over time in Python
"""
- Prior to Python 3.7 dictionaries DID NOT keep entries in the order of insertion
- Python 3.7 (2018) and later dictonaries keep entries in the order they were inserted
- "insertion order" is not "always sorted order"
"""
## Below the Abstraction
"""
- Python lists, dictionaries, and tupes are "abstract objects" designed to be easy to use
- For now we will just understand them and use them and thank the creators or Python for making them easy for us
- Using Python collections is easy. Creating the code to support them is tricky and uses Computer Scince concepts like dynamic memory, arrays, linked lists, hash maps and trees
"""
## Lists (Review)
"""
- We append values to the end of a List and look them up by position
- We insert values into a Dictionary using a key and retrieve them using a key
"""
cabinet = dict()
cabinet["summer"] = 12
cabinet["fall"] = 3
cabinet["spring"] = 75
print(cabinet)
cabinet['fall'] = cabinet['fall'] + 2
print(cabinet)
## Comparing Lists and Dictionaries
"""
Dictionaries are like lists except that they use keys insted of numbers to look up values
"""
## Dictionary Literals (Constants)
"""
- Dictinary  literals use curly braces and have a list of key : value pairs
- You can make an empty dictionary using empty curly braces
"""
jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
print(jjj)
ooo = {}
print(ooo)

## Many Counters with a Dictionary
"""
One common use of dictionaries is counting how often we "see" something
"""
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)
## Dictionary Tracebacks
"""
- It is an error to reference a key whicg is not in the dictionary
- We can use the in operator to see if a key is in the dictionary
"""
ccc = dict()
print('csev' in ccc)
## When We See a New Name
"""
When we encounter a new name, we need to add a new entry in the dictionary and if this the second or later time we have seen the name, 
we simply add one to the count in the dictionary under that name
"""
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)
## The get Method for Dictionaries
"""
The pattern of checking to see if a key is already in dictionary and assuming a default value if the key is not there
is so common that there is a method called get() that does this for us

Default value if key doesn't exists (and no Traceback)
"""
if name in counts:
    x = counts[name]
else:
    x = 0

x = counts.get(name, 0)

## Simplified Counting with get()
"""
We can use get() and provide default value of zero when the key is not in the dctionary - and then just add one
"""
counts = dict()
names =  ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)


# Dictionaries and Files
## Counting Patter
"""
The general pattern to count the words in a line of text is to split the line into words,
then loop through the words and use a dictionary to track the count of each word independently.
"""
counts = dict()
print('Enter a line of text:')
line = input('')
words = line.split()
print('Words:', words)
print('Counting ...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

##Define Loops and Dictionaries
"""
Even though dictionaries are not stored in order, we can write a for loop that goes through all the entries in a dictinary - 
actually it goes through all of the keys in the dictionary and looks up the values
"""
counts = {'chuck': 1, 'fred': 42, 'jan': 100}
for key in counts:
    print(key,counts[key])
##Rretrieving lists of Keys and Values
"""
You can get a list of keys, values, or items(both) from a dictionary
"""
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
print(list(jjj))
print(list(jjj.keys()))
print(list(jjj.values()))
print(list(jjj.items()))
## Bonus: Two Iteration Variables!
"""
- We loop through the key-value pairs in a dictionary using *two* iteration variables
- Each iteration, the first variable is the key and the second variable is the corresponding value for the key
"""
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
for aaa, bbb in jjj.items():
    print(aaa, bbb)