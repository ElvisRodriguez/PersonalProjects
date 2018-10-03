"""
Given a string, write a function to determine if it is a palindrome.
"""

def normalize(string):
    string = string.lower()
    string = "".join([s for s in string if s.isalpha()])
    return string

def is_palindrome(string):
    string = normalize(string)
    n = len(string)
    if n == 0:
        return True
    if string[0] == string[n-1]:
        return is_palindrome(string[1:n-1])
    else:
        return False

print(is_palindrome("racecar"))
print(is_palindrome("dolphin"))
print(is_palindrome("Dammit I'm mad"))
