def sum (n,m):
    if n == 0:
        return m
    return (n + sum (0,m))
print (sum (10,10))