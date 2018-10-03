"""
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1
(e.g. "waterbottle" is a rotation of "erbottlewat").
"""

def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 = s1.lower()
    s2 = s2.lower()
    j = s2.index(s1[0])
    for i in range(len(s1)):
        if s1[i] != s2[j]:
            return False
        j += 1
        j %= (len(s2))
    return True

def is_rotation2(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 = s1.lower()
    s2 = s2.lower()
    for i in range(len(s1)):
        if s1 == s2:
            return True
        s2 = s2[-1] + s2[:-1]
    return False

print(is_rotation("waterbottle", "erbottlewat"))
print(is_rotation2("waterbottle", "erbottlewat"))
