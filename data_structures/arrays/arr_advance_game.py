"""
Array Advance Game
Given an array of non negative integers, your starting position is the first
position of the array, with its value determining how many positions you can
move to the right, the position you chose to land on next determines your
next max amount of possible moves, so on, so forth etc.

Write a function that takes an array of non negative integers and returns
True if the "game" can be "won" using that array or False if it can't.
"""

# My initial (brute force-ish) approach
# Runtime: O(n^2)
# Corner case missed: instances where the max value leads to a
# false negative, such as the case with this array [3,3,1,2,0,2,0,0]
def arr_adv_game(arr):
    current = 0
    if arr[current] == 0:
        return False
    while current < len(arr) - 1 and arr[current] != 0:
        furthest = (current + arr[current] + 1)
        if furthest > len(arr):
            furthest = len(arr)
        max = -1
        next_pos = current
        for i in range(current + 1, furthest):
            if arr[i] >= max:
                max = arr[i]
                next_pos = i
        current = next_pos
    if arr[current] == 0:
        return False
    return True

# Second approach (not by me)
# Runtime: O(n)
# Catches the corner cased that my approach missed.
def array_advance(A):
    furthest_reached = 0
    last_idx = len(A) - 1
    i = 0
    while furthest_reached <= last_idx and furthest_reached >= i:
        furthest_reached = max(furthest_reached, A[i] + i)
        i += 1
    return furthest_reached >= last_idx
