def fib(n):
    a = 0
    b = 1
    
    for k in range(n):
        c = b+a
        a = b
        b = c
        
    return a

print(fib(8))

