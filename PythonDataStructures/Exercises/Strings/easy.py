# 1-3

#1 / Reverse a String
"""
Write a function that takes a string and returns it reversed.
"""

def myReverse( text ):
    return text[: : -1]
a = "hello"
print(myReverse(a))

#2 / Count Vowels
"""
Count the number of vowels (a, e, i, o, u) in a given string.
"""
def countVowels(text):
    vowels = "aeiou"
    count = 0
    for i in text:
        if i in vowels:
            count = count + 1
    return count
a = 'eaiuoukfhuetuvjsag'
print(countVowels(a))

#3 / Check for Substring
"""
Check if a specific word or character exists within a string
"""
str = input('Input string:')
subStr = input('Input word or character:')
if subStr in str:
    print('It was substring')
else:
    print('It was not substring')