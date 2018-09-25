"""
Given a sorted array of integers and an integer (named target), return two
elements of the array such that their sum is equal to target.
You can assume that all arrays will have exactly one solution.
You may not use the same element twice.

Example:
input = [-2, 1, 2, 4, 7, 11], 13
output = [2, 11]
"""

# First Approach:
# Time complexity: O(n)
# Space complexity: O(n)
def two_sum_hash_table(array, target):
    hash_table = dict()
    for i in range(len(array)):
        if array[i] in hash_table:
            return hash_table[array[i]], array[i]
        hash_table[target - array[i]] = array[i]
    return None

# Second Approach:
# Time complexity: O(n)
# Space complexity: O(1)
def two_sum(array, target):
    i = 0
    j = len(array) - 1
    while i != j and i < j:
        if array[i] + array[j] == target:
            return array[i], array[j]
        if array[i] + array[j] < target:
            i += 1
        else:
            j -= 1
    return None

print(two_sum_hash_table([-2, 1, 2, 4, 7, 11], 13))
print(two_sum([-2, 1, 2, 4, 7, 11], 13))
