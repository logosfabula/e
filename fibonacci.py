def fib(acc, acc2, n):
    if n <= 0:
        return acc
    else:
        return fib(acc2, acc+acc2, n-1)

for i in range (15):
    print(fib(0,1,i))
