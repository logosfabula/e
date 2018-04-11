# factorial

def fact_tail_help(n, acc):
    if (n<=1):
        return acc
    else:
        return fact_tail_help(n-1, acc * n)

def fact_tail(n):
    return fact_tail_help(n,1)

def fact_norm(n):
    if (n<=1):
        return 1 
    else:
        return fact(n-1) * n 

fact_norm(10000)
fact_tail(10000)
