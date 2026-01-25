"""
Functions
"""
#--Using Function--#
"""
Stored (and reused) Steps

Program:            Output:
def thing():
    print('Hello')
    print('Fun')

thing()             Hello
                    Fun
print('Zip')        Zip
thing()             Hello
                    Fun
"""

#Max Function
"""
A function is some stored code that we use.
A function takes some input and produces an output.
"""

big = max('Hello world')
print(big)

#Type Conversions
"""
- When you put an integer and floating point in an expression,
the integer is implicitly converted to a float.
- You can control this with the built-in functions int() and float()
"""

#String Conversion
"""
- You can also use int() and float() to covert between strings and integers
- You will get an error if the string does not contain numeric characters
"""


##--Building Functions--##

"""
Building our Own Functions
- We create a new function using the def keyword followed by optional parameters in parentheses
- We indent the body of the function
- This defines the function but foes not execute the body on the function
"""
print('Hello')

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

print('Yo')

#Arguments
"""
- An argument is a value we pass into the function as its input when we call the function
- We use arguments so we can direct the function to do different kind of work when we call it at different times
- We put the argument in parentheses after the name of the function

big = max('Hello world')

('Hello world' is the argument)
"""

#Parameters
"""
A parameter is a variable which we use in the function definition.
It is a "handle" that allows the code in the function to access the arguments for a particular function invocation.

def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print("Hello")

>>>greet('en')
Hello
>>>greet('es')
Hola
>>>greet('fr')
Bonjour
"""

#Return Values
"""
Often a function will take its arguments, do some computation, 
and return a value to be used as the value of the function call in the calling expression.
The return keyword is used for this.

def greet():
    return "Hello"

>>>print(greet(), "Glenn")
Hello Glenn

- A "fruitful" function is one that produces a result (or return value)
- The return statement ends the function execution and "sends back" the result of the function
"""

#Multiple Parameters / Arguments
"""
- We can define more than one parameter in the function definition
- We simply add more arguments when we call the function
- We match the number and order of arguments and parameters
"""
