#4-15

#4 / Palindrome Checker
"""
Determine if a string reads the same forwards and backwards
"""
def isPolindrome(word):
    return word == word[::-1]

text = 'katakik'
print(isPolindrome(text))

#5 / Capitalize Words
"""
Capitalize the first of every word in a sentence.
"""
sent = "Capitalize the first of every word in a sentence."
res = " ".join([w.capitalize() for w in sent.split()])
print(res)
