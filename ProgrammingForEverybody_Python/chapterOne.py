##--Elements of Python--##
"""
- assignment statement
x = 2

- assignment with expression
x = x + 2

- print function
print(x)
"""


##--Writing Paragraphs of Code--##
"""
Program Steps or Program Flow
- Like a receipe or installation instructions, a program is a SEQUENCE of steps to be done in order.
- Some steps are CONDITIONAL - they may be skipped.
- Sometimes a step or group of steps is to be REPEATED.
- Sometimes we store a set of steps to be used over and over as needed sereval places throughout the program
"""
#Sequential Steps:
"""
x = 2
print(x)
x = x + 2
print(x)

- When a program is running, it flows from one step to the next.
"""

#Conditional Steps:
"""
x = 5
if x < 10:
    print("Smaller")
if x > 20:
    print("Bigger")
print("Finish")
"""

#Repeated Steps:
"""
n = 5
while n > 0:
    print(n)
    n = n - 1
print("Blastoff")

- Loops (repeated steps) have ITERATION VARIABLES that change each time through a loop
"""

#A short Python "Story" about how to count words in a file:

#Get the name of the file and open it
name = input('Enter file:')
handle = open(name, 'r')

#Count word frequency
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

#Find the most common word
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

#All done
print(bigword, bigcount)