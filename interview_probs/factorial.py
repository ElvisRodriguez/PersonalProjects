"""
Implements an iterative and recursive method to find the factorial of an
integer n
"""

def fact_recursive(n):
    if n <= 1:
        return 1
    return n * fact_recursive(n-1)

def fact_iterative(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

print(fact_iterative(5))
print(fact_recursive(5))
