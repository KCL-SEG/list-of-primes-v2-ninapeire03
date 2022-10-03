"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isPrime(n):
    isPrime = True
    for i in range (2,n):
        if n != 2 and n%i == 0:
            isPrime = False
    return isPrime

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("You should enter a value greater or equal to 1.")
    list = []
    n = 2
    while (len(list) < number_of_primes):
        if isPrime(n):
            list.append(n)
        n += 1
    return list
