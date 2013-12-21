#!/usr/bin/env python


def fact(n):
    '''
    returns the factorial of a number
    n is in the range [1..2,000]
    use iterative solution instead of recurive to prevent
    hitting stack overflow (reached recursive depth) error
    '''
    num = 1
    while n >= 1:
        num = num * n
        if num % 5 == 0:
            # if num is exactly divisble by 5, get rid of zeroes
            # as they do not add anything in the sum
            # huge speed gains + less like to overflow!!
            num /= 10
        n = n - 1
    return num

def solution(n):
    fac = fact(n) # get the factorial of the number
    dig_sum = sum([int(i) for i in str(fac)])
    return -1 if dig_sum > 100000000 else dig_sum