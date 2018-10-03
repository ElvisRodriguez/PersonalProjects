"""
Given an array of integers where every element appears twice except for one,
find that one.
Solution should be O(n) time complexity, O(1) space complexity
"""

def single_num(integers):
    result = 0
    for i in range(len(integers)):
        result ^= integers[i]
    return result

print(single_num([3, 3, 2, 2, 1]))
