#Memoization

def fib(n, memo):
  if n == 0:
    return 0
  if n == 1:
    return 1
  if n in memo:
    return memo[n]
  memo[n] = fib(n-1, memo) + fib(n-2, memo)
  return fib(n-1, memo) + fib(n-2, memo)

# fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]

# for i in range(len(fibs)):
#   print(fibs[i] == fib(i, {}))

print(fib(50, {}))
