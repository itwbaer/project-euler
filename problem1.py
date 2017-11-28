"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def is_divisible_by(n, d):
    # if the remainder is equal to 0, then n is divisible by d
    print(True if n % d == 0 else False)
    return True if n % d == 0 else False


def sum_of_multiples(lowerLimit, upperLimit, divisors):
    multSum = 0

    for n in range(lowerLimit, upperLimit+1):
        #for each divisor, test if n divisible by it
        for d in divisors:
            if is_divisible_by(n, d):
                multSum = (multSum + n)
                break
        print(n)
    return multSum


divisors = [3, 5]
print(sum_of_multiples(1, 1000, divisors))