"""
Write a function that takes a sorted list and a key and returns the index of
the first occurence of the key.
"""

def bin_search(arr, key):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l+r)//2
        if key == arr[m]:
            return arr.index(arr[m])
        if key > arr[m]:
            l = m + 1
        elif key < arr[m]:
            r = m - 1
    return -1

test = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]

for t in test:
    print(bin_search(test, t))
