# Files

## Opening a File
"""
- Before we can read the contents of the file, we must tell Python which file we are going to work with and what we will be doing with the file
- This is done with the open() function
- open() returns a "file handle" - a variable used to perform operations on the file
- Similar to "File -> Open" in Word Processor
"""
## Using open()
"""
- handle = open(filename, mode)
- returns a handle use to manipulate the file
- filename is a string
- mode is optional and should be 'r' if we are planning to read the file and 'w' if we are going to write to the file
"""
## What is a Handle?
"""
fhand = open('mbox.txt')
print(fhand)
"""
## The newline Character
"""
- We use a special character called the "newline" to indicate when a line ends
- We represent it as \n in string
- Newline is still one character - not two
"""
stuff = 'Hello\nWorld'
print(stuff)
print(len(stuff))

# Processing Files
## File Handle as a Sequence
"""
- A file handle open for read can be treated as a sequence of string where each line in the file is a string in the sequence
- We can use the for statement to iterate through a sequence
- Remember - a sequence is an ordered set

xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)
"""
## Counting Lines in a File
"""
- Open a file read-only
- Use a for loop to read each line
- Count the lines and print out the number of lines

fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = couut + 1
print('Line Count: ', count)
"""
## Reading the *Whole* File
"""
We can read the whole file (newlines and all) into a single string
fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])
"""
## Searching Through a File
"""
We can put an if statement in out for loop to only print lines that meet some criteria

fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From: '):
        print(line)

What are all blank lines doing here?
- Each line form the file has a newline at the end
- The print statement adds a newline to each line
"""
## Searching Through a File (fixed)
"""
- We can strip the whitespace from the right-hand side of the string using rstrip() from the string library
- The newline is considered "white space" and is stripped

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From: '):
        print(line)
"""
## Skipping with Continue
"""
We can conveniently skip a line by using the continue statement

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From: '):
        continue
    print(line)
"""
## Using in to Select lines
"""
We can look for a string anywhere in a line as our selection criteria

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)
"""
## Prompt for File Name
"""
fname = input('Enter the file name: ')
fhand =  open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were ', count, 'subject lines in ', fname)
"""
## Bad File Names
"""
fname = input('Enter the file name: ')
try:
    fhand =  open(fname)
except:
    print('File cannot be opened: ', fname)
    quit()
    
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were ', count, 'subject lines in ', fname)
"""