"""
Given an array of integers, determine which pair of elements has the highest
difference between the second element of the pair and the first.
The pairs must be a subset of the array, therefore maintaining the order of
the array.

example:
input = [30, 35, 29, 20, 32]
output = [20, 32]
([20, 35] is not valid because 35 comes before 20 in the array)
"""

# Brute Force approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def stocks(array):
    profit = 0
    market = dict()
    market[profit] = 0
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[j] - array[i] > profit:
                profit = array[j] - array[i]
                market[profit] = array[i], array[j]
    return market[profit]

# Second approach
# Time Complexity: O(n)
# Space Complexity: O(1)
def buy_and_sell(array):
    profit = 0
    for i in range(len(array)):
        if array[i] - min(array[0:i+1]) > profit:
            profit = array[i] - min(array[0:i+1])
    return profit

print(buy_and_sell([310,315,275,295,260,270,290,230,255,250]))
