"""
Given a string, return the 'compressed' version of that string.
If a compressed string is not any smaller than the original string, return the
original string. Input will only consist of [a-zA-Z]
e,g,
'aaabbcccccdd' = 'a3b2c5d2'
"""

def compress(string):
    result = ""
    count = 1
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            count += 1
        else:
            result += string[i] + str(count)
            count = 1
    result += string[i+1] + str(count)
    if len(result) >= len(string):
        return string
    return result

print(compress('aaabbcccccd'))
