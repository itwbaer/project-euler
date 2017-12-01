"""	Largest palindrome product
	Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

"""
    Will need function to test for palindrome

    Brute Force: For every combination of two 3-digit numbers, test if palindrome
    Inverse would be faster because we dont have to do a n2 loop:
    For every palindrome, check if it factorizes to two 3-digit numbers

"""


def is_palindrome(n):
    # convert to string
    str_n = str(n)

    # reverse the string
    rev_str_n = str_n[::-1]

    # convert back to number and compare
    palindrome = int(rev_str_n)

    return True if n == palindrome else False


def largest_palindrome(n, d):
    """ based on number of digits, we can know where to start looking
    d-1 would be how many 0's there are in one number, multiplied by how many numbers there are
    raise to the power of ten
    """
    smallest = 10 ** ((d - 1) * n)
    largest = 10 ** (((d + 1) - 1) * n) - 1


print(largest_palindrome(2, 3))