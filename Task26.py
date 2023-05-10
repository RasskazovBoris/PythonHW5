def f (n):
    if n == 1:
        return 1
    return n * f(n-1)
print (f(5))

def sum (n):
    if n == 0:
        return 0
    return n + sum(n-1)
print (sum(10))