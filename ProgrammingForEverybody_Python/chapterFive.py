##--Loopes and Iteration--##

#Repeted Steps
"""
Loops (repeated steps) have iteration variables that change each time through a loop.
Often these iteration variables go through a sequence of numbers.

n = 5
while n > 0:
    print(n)
    n = n - 1
print("Blastoff!")
print(n)
"""

#An Infinite Loop
"""
n = 5
while n > 0:
    print('Hello')
print('End')
"""

#Breaking Out of a Loop
"""
- The break statement ends the current loop and jumps to the statement immediately following the loop.
- It is like a loop test that can happen anywhere in the body of the loop
"""
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

#Finishing an Iteration with Continue
"""
The continue statement ends the current iteration and jumps to the top of the loop and starts the next iteration
"""
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')


##--Definite Loops--##
"""
A Simple Definite Loop

for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')

A Definite Loop with Strings

friends = [Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year: ', friend)
print('Done!')

- Definite loops (for loops) have explicit iteration variables that change each time through a loop.
These iteration variables move through the sequence or set
"""

#Looking at In ...
"""
- The iteration variable "iterates" through the sequence (orgered set)
- The block (body) of code is executed once for each value in the sequence
- The iteration variable moves through all of the values in sequence
"""

##--Finding the Largest Value--##

#Making "smart" Loops
"""
The trick is "knowing" something about the whole loop when you are stuck writing code that only sees one entry at a time
"""

#Finding the Largest Value
"""
We make a variable that contains the largest value we have seen so far.
If the current number we are looking at is larger, it is the new largest value we have seen so far.
"""
largest_so_far = -1
print("Before", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print("After", largest_so_far)

#The "is" and "is not" Operators
"""
- Python has an is operator that can be used in logical expressions
- Implies "is the same as"
- Similar to, but stronger than ==
- is not also is a logical operator
"""
