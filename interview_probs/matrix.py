"""
Given an N cross M matrix in which each row is sorted, find the overall median
of the matrix. Assume N x M is odd
e.g.
Matrix:
[1,3,5]
[2,6,9]
[3,6,9]

Actual input is a list of lists
"""

#2n-1 2n-1 4n2 -4n + 1

def median_matrix(matrix):
    total = matrix[0]
    for k in range(1, len(matrix)):
        m = matrix[k]
        temp = []
        i = 0
        j = 0
        while i < len(total) and j < len(m):
            if total[i] < m[j]:
                temp.append(total[i])
                i += 1
            else:
                temp.append(m[j])
                j += 1
        while i < len(total):
            temp.append(total[i])
            i += 1
        while j < len(m):
            temp.append(m[j])
            j += 1
        total = temp
    return total[len(total) // 2]

print(median_matrix([[1,3,5], [2,6,9], [3,6,9]]))
