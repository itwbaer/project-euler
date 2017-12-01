""" Largest prime factor
    Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


""" Primality
notes from wikipedia: https://en.wikipedia.org/wiki/Primality_test
    
Brute force would be to test all n

Only need test numbers less than or equal to sqrt(n) or redundent
Can skip all even numbers greater than 2 because they can be reduced by 2

Primes of the form 6k +- 1
Test 2 and 3, then test 6k +- 1 <= sqrt(n)

"""


import math


def is_prime(n):
    # base cases
    # 1 or less not prime
    if n <= 1:
        return False
    #2 or 3 is prime
    elif n <= 3:
        return True
    #even is not prime
    elif n % 2 == 0:
        return False

    # run algorithm
    k = 6
    while k * k <= n:
        if n % (k - 1) or n % (k + 1):
            return False
        k = k + 6
    return True


""" Brute force would be to test all numbers 1 to n-1 to see if it divides n
    All factors have a pair, so only need to test half of numbers
    We can start closer to original number because we are looking for largest
    Largest possible factor would the pair with 2
"""


def largest_prime_factor(n):
    # if the number itself is prime can exit right away
    if is_prime(n):
        return -1

    # define pairs we will need to check later
    pairs_to_check = list()

    for i in range(int(math.floor(n/2)), int(math.floor(math.sqrt(n))), -1):

        #first check if factor
        if n % i == 0:
            print(i)
            if is_prime(i):
                return i
            #add pair to pair list
            pairs_to_check.append(n / i)

    # We didnt find largest prime, check one last time in pair list
    for i in pairs_to_check:
        if is_prime(i):
            return i

    # Didn't find a prime
    return -1


print(largest_prime_factor(600851475143))
