'''
Solving a combination (n choose k) problem using 2 methods:
- Factorial formula
- Pascal's Triangle
Seems that generating a pascal triangle if more efficient in terms of time
complexity, but loses to factorial in space complexity
'''

import time

#time complexity O(n^2)
#space complexity O(n^2)
def pascal_triangle(size):
    if size == 1:
        return [[1]]
    triangle = [[1],[1,2,1]]
    if size == 2:
        return triangle
    while size > 2:
        prev_line = triangle[-1]
        if len(prev_line) % 2 == 1:
            line = []
            middle = len(prev_line) // 2
            for i in range(0, middle):
                line.append(prev_line[i] + prev_line[i+1])
            for i in range(middle, len(prev_line) - 1):
                line.append(prev_line[i] + prev_line[i+1])
            line = [1] + line + [1]
            triangle.append(line)
            size -= 1
        elif len(prev_line) % 2 == 0:
            line = []
            middle_b = len(prev_line) // 2
            middle_a = middle_b - 1
            for i in range(0, middle_a + 1):
                line.append(prev_line[i] + prev_line[i+1])
            for i in range(middle_b, len(prev_line) - 1):
                line.append(prev_line[i] + prev_line[i+1])
            line = [1] + line + [1]
            triangle.append(line)
            size -= 1
    return triangle

#time complexity O(n)
#space complexity O(1)
def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def choose_pascal(n, k):
    triangle = pascal_triangle(n)
    answer_line = triangle[n-1]
    return answer_line[k]

def choose_factorial(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

if __name__ == '__main__':
    start_a = time.time()
    choose_pascal(1000,500)
    end_a = time.time()
    start_b = time.time()
    choose_factorial(1000,500)
    end_b = time.time()
    pascal_time = end_a - start_a
    factorial_time = end_b - start_b
    if pascal_time > factorial_time:
        print('Pascal Wins')
    else:
        print('Factorial Wins')
