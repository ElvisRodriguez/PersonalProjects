"""
Implement an algorithm to detect if a string has unique characters.

Example:
'Python' --> True
'Racecar' --> False
'12345' --> True
'Aaron' --> False

Upper and lower case characters are treated as the same character, e.g. A == a
"""

def is_unique(string):
    string = string.lower()
    chars = ""
    for char in string:
        if char in chars:
            return False
        chars += char
    return True

for s in ['Python', 'Racecar', '12345', 'Aaron']:
    print(is_unique(s))
