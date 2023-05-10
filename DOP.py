def fib (n):
    m = n - 1
    if m == 0:
        return 0
    if m == 1:
        return m
    return fib (n-1) + fib (n-2)

print (fib (10))