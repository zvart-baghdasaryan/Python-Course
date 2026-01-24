##--Constants, Reserved Words & Variables--##

#Constants:
"""
FIXED VALUES such as numbers, letters, and strings, are called "constants" because their value does not change
- Numeric constants are as you expect
- String constants use single quotes (') or doube quotes (")
"""

#Reserved Words:
"""
You cannot use reserved words as variable names / identifiers
E.g False, None, True, and, as, ...
"""

#Variabls:
"""
- A variable is a named place in the memory where a programmer can store data and later retrieve the data using the variable "name"
- Programmers get to choose the names of the variables
- You can change the contents of a variable in a later statement
"""

#Python Variable Name Rules:
"""
- Must start with a letter or underscore _
- Must consist of letters, numbers, and underscores
- Case Sensitive
"""

#Sentences or Lines:
"""
x = 2       # Assignment statement
x = x + 2   # Assignment with expression
print(x)    # Print statement
"""


##--Variable Names and Assignment--##

#Assignment Statements:
"""
- We assign a value to a variable using the assignment statement (=)
- An assignment statement consists of an expression of the right-hand side and a variable to store the result

x = 3.9 * x * (1 - x)
- A variable is a memory location used to store a value
- The right side is an expression. 
Once the ecpression is evaluated, the result is places in (assigned to) x.
"""

##--Numerical Expressions--##

#Numerical Expressions:
"""
- Because of the lack of mathematical symbols on computer keyboards - we use "computer-speak" to express the classic math operations

Operator    Operation

+           Addition
-           Subtraction
*           Multiplication
/           Devision
**          Power
%           Remainder

"""

#Order of Evaluation:
"""
- When we string operators together - Python must know which one to do first
- This is called "operator precedence"
"""

#Operator Precedence Rules
"""
Highest precedence rule to lowest precedence rule:
- Parentheses are always respected
- Exponentiation (raise to power)
- Multiplication, Division, and Remainder
- Addition and Subtraction
- Left to right
"""


##--Variable Types--##

#What does "Type" Mean?
"""
- In Python variables, literals, and constants have a "type"
- Python knows the difference between an integer number and a string
- For example "+" means "addition" if something is a number and "concatenate" if something is a string
"""

#Type Matters:
"""
- Python knows what "type" everything is
- Some operations are prohibited
    - You cannot "add" 1 to a string
- We can ask Python what type something is by using the type() function
"""

#Several Types of Numbers:
"""
Numvers have two main types
- Integers are whole numbers:
    -14, -2, 0, 1, 100
- Floating Point Numbers have decimal parts:
    -2.5, 0.0, 98.6
There are other number types - they are variation on float and integer
"""

#Type Conversions:
"""
- When you put an integer and floating point in an expression, the integer is implicitly converted to a float
- You can control this with the built-in function int() and float()
"""

#Integerr Division:
"""
- Integer division produces a floating point result
    print(10 / 2)
    5.0
"""

#String Conversions
"""
- You can also use int() and float() to convert between string and integers
- You will get an error if the string does not contain numeric characters
"""

#User Input
"""
- We can instruct Python to pause and read data from the user using the input() function
- The input() function returns a string
"""


##--Writing Comments in Python--##

#Comments in Python:
"""
Anything after # is ignored by Python

Why Comment?
- Describe what is going to happen in a sequence of code
- Document who wrote the code or other ancillary information
- Turn off a line of code - perhaps temporarly
"""

##--First I-O-P Program--##
"""
Converting User Input
- If we want to read a number from the user, we must convert it from a string to a number using a type conversion fnction
- Later we will deal with bad input data
"""

#Convert elevator floors
inp = input('Europe floor?')
usf = int(inp) + 1
print('US floor', usf)