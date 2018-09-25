"""
Arbitray precision problem
Given an array of non negative integers less than 10 that represent one integer,
return an array that is the sum of the given "integer" + 1.
Example:
input = [1, 4, 9] -> output = [1, 5, 0]
input = [9, 9] -> output = [1, 0, 0]
"""

def precision_prob(arr):
    if arr[-1] < 9:
        arr[-1] += 1
        return arr
    i = len(arr) - 1
    while i >= 0:
        arr[i] += 1
        if arr[i] == 10:
            arr[i] = 0
            if i == 0:
                return [1] + arr
        else:
            return arr
        i -= 1

print(precision_prob([1,4,9]))
print(precision_prob([1,9,9]))
print(precision_prob([9,9,9]))
