def factorial(n):
    if n < 0:
        raise ValueError('Factorial is defined only for nonnegative numbers')
    total = 1
    for i in range(1,n+1):
        total *= i
    return total

print(factorial(-1))