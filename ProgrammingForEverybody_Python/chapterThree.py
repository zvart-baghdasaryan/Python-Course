##--Conditional Statements--##

#Comparison Operators
"""
- Boolean expressions ask a question and produce a Yes or No result which we use to control program flow
- Boolean expressions using comparison operators evaluate to True / False or Yes / No
- Comparison operators look at variables but do not change the variables

Python      Meaning

<           Less than
<=          Less than or Equal to
==          Equal to
>=          Greater than
>           Greater than
!=          Not equal

Remember: "=" is used for assignment.
"""

x = 5
if x == 5:
    print('Equals 5')
if x > 4:
    print('Greater than or Equals 5')
if x < 6: print('Less than 6')
if x <= 5:
    print('Less than or Equal 5')
if x != 6:
    print('Not equal 6')

#Nested Decisions:
x = 42
if x > 1:
    print("More than one")
    if x < 100:
        print("Less than 100")
print("All done")

#Two-way Decisions:
"""
- Sometimes we want to do one thing if a logical expression is tru and something else if the expression is false
- It is like a fork in the road - we must choose one or the other path but not both
"""

x = 4
if x > 2:
    print('Bigger')
else:
    print('Smaller')
print('All Done')

#Multi-way:

if x < 2:
    print('Small')
elif x < 10:
    print('Medium')
else:
    print('Large')
print('All done')

#The try / except Structure
"""
- You surround a dangerous section of code with try and except
- If the code in the try works - the except is skipped
- If the code in the try fails - it jumps to the except section 

astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1
"""

astr = 'Bob'
try:
    print('Hello')
    istr = int(astr)
    print('There')  #This line of code should not execute
except:
    istr = -1

print('Done', istr)

