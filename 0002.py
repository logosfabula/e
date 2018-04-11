'''
Even Fibonacci numbers
Problem 2 
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

def fibonacci_sum_of_evens_under_fourmillion():
    sum = 0
    tab = {}
    tab[0] = 1
    tab[1] = 1
    i = 2
    while True: 
        tab[i] = tab[i-1] + tab[i-2] 
        if tab[i] % 2 == 0:
            sum = sum + tab[i]
        if tab[i] > 4000000:
            return sum
        i = i + 1

fibonacci_sum_of_evens_under_fourmillion()
