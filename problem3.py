""" Largest prime factor
    Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


""" notes from wikipedia
    
Brute force would be to test all n

Only need test numbers less than or equal to sqrt(n) or redundent
Can skip all even numbers greater than 2 because they can be reduced by 2

Primes of the form 6k +- 1
Test 2 and 3, then test 6k +- 1 <= sqrt(n)

"""


def is_prime(n):
    #base cases
    #1 or less not prime
    if n <= 1:
        return False
    #2 or 3 is prime
    elif n <= 3:
        return True
    #run algorithm
    

def largest_prime_factor(n):

    return 0


print(largest_prime_factor(600851475143))
