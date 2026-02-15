#Strings
"""
- A string is a sequence of characters
- A string literal uses quotes 'Hello' or "Hello"
- For strings, + means "concatenate"
- When a string contains numbers, it is still a string
- We can convert numbers in a string into a number using int()
"""
str1 = "Hello"
str2 = 'there'
str3 = '123'
x = int(str3) + 1
print(x)

"""
Reading and Converting
- We prefer to read data in using string and then parse and convert the data as we need
- This gives us more control over error situations and/or bad user input
- Input numbers must be converted from strings
"""
name = input('Enter:')
print(name)
apple = input('Enter:')
print(int(apple) - 10)

"""
Looking Inside Strings
- We can get at any single character in a string using an index specified in square brackets
- The index value must be an integer and starts at zero
- The index value can be an expression that is computed
"""
fruit = 'banana'
print(fruit[1])
x = 5
print(fruit[x - 1])

"""
A character Too Far
- You will get a python error if you attempt to index beyond the end of a string.
- So be careful when constructing index values and slices

>>> zot = 'abc'
>>> print(zot[5])
Traceback ....
"""

"""
Strings Have Length
The buit-in function len gives us the length of a string
"""
fruit = 'banana'
print(len(fruit))

"""
Len Function
A function is some stored code that we use. A function takes some input and produces an output.
"""

#Looping Through Strings
"""
Using a while statement and an iteration variable, and the len function, 
we can construct a loop to took at each of the letters in a string individually
"""
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

"""
- A definite loop using a for statement is much more elegant
- The iteration variable is completely taken care of by the for loop
"""
fruit = 'banana'
for letter in fruit:
    print(letter)

"""Looping and Counting"""
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

"""
Looking Deeper into in
- The iteration variable "iterates" through the sequence (ordered set)
- The block (body) of code is executed once for each value in the sequence
- The iteration variable moves through all of the values in the sequence

for 
The iteration variable "iterates through the string and the block (body) of code is executed once for each value in the sequence"
"""

#Slicing Strings
"""
- We can also look at any continuous section of a string using a colon operator
- The second number is one beyond the end of the slice - "up to but not including"
- If the second number is beyond the end of the string, it stops at the end
"""
s = "Monty Python"
print(s[0:4])   #Mont
print(s[6:7])   #P
print(s[6:20])  #Python

"""
If we leave off the first number or the last number of the slice,
it is assumed to be the beginning or end of the string respectively
"""
s = 'Monty Python'
print(s[:2])    #Mo
print(s[8:])    #thon
print(s[:])     #Monty Python

#Manipulating Strings
"""
When the + operator is applied to strings, it means "concatenation"
"""
a = 'Hello'
b = a + 'There'
print(b)        #HelloThere
c = a + ' ' + 'There'
print(c)        #Hello There

#Using in as a Logical Operator
"""
- The in keyword can also be used to check to see if one string is "in" another string
- The in expression is a logical expression that return True or False and can be used in an if statement
"""

fruit = "banana"
'nan' in fruit
if 'a' in fruit:
    print('Found it!') 

#String Comperison
if word == 'banana':
    print('All right, bananas.')

if word < 'banana':
    print('Your word, ' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word, ' + word + ', comes after banana.')
else:
    print('All right, bananas.')

#String Library
"""
- Python has a number of string functions which are in the string library
- These functions are already built into every string - we invoke them by appending the function to the string variable
- These functions do not modify the original string, instead they return a new string that has been altered
"""
greet = "Hello Bob"
zap = greet.lower()
print(zap)
print('Hi There'.lower())

stuff = 'Hello world'
print(type(stuff))
"""<class 'str'>"""
print(dir(stuff))
"""methods in the class str"""

"""
String Library
str.capitalize()
str.center(width[, fillchar])
str.endswith(suffix[, start[, end]])
str.find(sub[, start[, end]])
str.lstrip([chars])
str.replace(old, new[, count])
str.lower()
str.rstrip([chars])
str.strip([chars])
str.upper()
"""

#Searching a String
"""
- We use the find() function to search for a substring within another string
- find() finds the first occurrence of the substring
- If the substring is not found, find() returns -1
- Remember that string position starts at zero
"""
fruit = 'banana'
pos = fruit.find('na')
print(pos)
aa = fruit.find('z')
print(aa)

#Making Everything Upper Case
"""
- You can make a copy of a string in lower or upper case
- Often when we are searching for a string using find() we first convert the string to lower case so we can search a string regardless of case
"""
great = 'Hello Bob'
print(great.upper())

#Search and Replace
"""
- The replace() function is like a 'search and replace' operation in a word processor
- It replaces all occurrences of the search string with the replacement string 
"""
great = 'Hello Bob'
nstr = great.replace('Bob', 'Jane')
print(nstr)

# Stripping Whitespace
"""
- Sometimes we want to take a string and remove whitespace at the beginning and/or end
- lstrip() and rstrip() remove whitespace at the left or right
- strip() removes both beginning and ending whitespace
"""
greet = '   Hello Bob  '
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())

#Prefixes
line = 'Please have a nice day'
print(line.startswith('Please'))
print(line.startswith('p'))

#Parsing and Extracting
data = 'From stephen.maruduard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos + 1 : sppos]
print(host)

"In Python 3, all strings are Unicode"