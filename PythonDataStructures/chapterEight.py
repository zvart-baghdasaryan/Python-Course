# Lists

## Programming
"""
Algorithms
- A set of rules or steps used to solve a problem
Data Structures
- A particular way of organize data in a computer
"""
## Which is Not A "Collection"?
"""
Most of our variables have one value in them - when we put a new value in the variable, the old value is overwritten
"""
## A List Is a Kind of Collection
"""
- A collection allows us to put many values in a single "variable"
- A collection is nice because we can carry many values around in one convenient package.

friends = ['Joseph', 'Glenn', 'Sally']
"""
## List Constants
"""
- List constants are surrounded by square brackets and the elements in the list are separated bu commas
- A list element can be any Python object - even another list
- A list can be empty
"""
for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff')
## Looking Inside Lists
"""
Just like strings, we can get at any single element in a list using an index specified in square brackets
"""
friends = ['Joseph', 'Glenn', 'Sally']
print(friends[1])
## Lists Are Mutable
"""
- Strings are "immutable" - we cannot change the contents of a string - we must make a new string to make any changes
- Lists are "mutable" -we can change an element of a list using the index operator
"""
lotto = [2, 14, 26, 41, 63]
print(lotto)
lotto[2] = 28
print(lotto)
## How Long is a List?
"""
- The len() function takes a list as a parameter and return the number of elements in the list
- Actually len() tells us the number of elements of any set or sequence (such as a string ...)
"""
x = [1, 2, 'joe', 99]
print(len(x))
## Using the Range Function
"""
- The rande function returns a list of numbers that range from zero to one less than the parameter
-  We can construct an index loop using for and an integer iterator
"""
print(range(4))
friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends))
print(list(range(len(friends))))


# Manipulating Lists

## Concatenating Lists Using +
"""
We can create a new list by adding two existing lists together
"""
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
## Lists Can Be Sliced Using :
"""
Remember: Just like in string, the second number is "up to but not including"
"""
t = [9, 41, 12, 3, 74, 15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])
## List Methods
x = list()
print(type(x))
print(dir(x))
## Buiding a List from Scratch
"""
- We can create an empty list and then add elements using the append method
- The list stays in order and new elements are added at the end of thee list
"""
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
## Is Something in a List?
"""
- Python provides two operators that let you check if an item is in a list
- These are logical operators that return True or False
- They do not modify the list
"""
some = [1, 9, 21, 10, 16]
print(9 in some)
print(15 in some)
print(20 not in some)
## Lists are in Order
"""
- A list can hold many items and keeps those items in the order until we do something to change the order
- A list can be sorted (i.e., change its order)
- The sort method (unlike in strings) means "sort yourself"
"""
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)
print(friends[1])
## Built-in Functions and Lists
"""
- There are a number of functions built into Python that take lists as parameters
- Remember the loops we built? These are much simpler.
"""
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))


#  Lists and String
"""
Split breaks a string into parts and produces a list of string.
We think of these as words.
We can access a particular word or loop throught all the words.

- When you do not specify a delimiter, multiple spaces are treated like one delimiter
- You can specify what delimiter character to use in the splitting
"""
line = 'A lit         of  spaces'
etc = line.split()
print(etc)
## The Double Split Pattern
"""
Sometimes we split a line one way, and grab one of the pieces of the line and split that piece again
"""
line = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])