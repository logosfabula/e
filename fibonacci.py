def fib_tail(acc, acc2, n):
    if n <= 0:
        return acc
    else:
        return fib_tail(acc2, acc+acc2, n-1)

def fib(n):
    fib_tail(0, 1, n)
    
for i in range (15):
    print(fib(0,1,i))
