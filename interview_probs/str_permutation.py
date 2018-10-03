"""
Given two string, write a function to determine if one is a permutation of the
other.
"""

def is_permutation(a, b):
    a = a.lower()
    b = b.lower()
    if len(a) != len(b):
        return False
    for char in a:
        if char not in b:
            return False
        if char in b:
            b = b.replace(char, '', 1)
    return True

print(is_permutation("dog", "god"))
print(is_permutation("not", "top"))
print(is_permutation("rer", "ree"))
