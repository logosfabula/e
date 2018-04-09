'''
Largest prime factor
Problem 3 
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
def largest_prime_factor(integer):    
    i = 1
    while i < integer: 
        i = i + 1
        if integer % i == 0:
            integer = integer / i
    return i
    
largest_prime_factor(600851475143)
            