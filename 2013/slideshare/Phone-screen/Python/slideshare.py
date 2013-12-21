#!/usr/bin/env python

'''
From the rightmost digit, which is the check digit, moving left, replace every
second digit with the result of the following; double the value; if product of
this doubling operation is greater than 9 (e.g., 5 * 2 = 10), then sum the
digits of the products (e.g., 10: 1 + 0 = 1, 14: 1 + 4 = 5).

Sum all of the digits. (e.g., 2 + 2 + 6 + 4 + 1 + 5 = 20)

If the sum modulo 10 is equal to 0 (if the total ends in zero) then the number
is valid; else it is not valid. (e.g., 20 % 10 = 0)

'''

def isValid(accountNumber):
    num = str(accountNumber)
    nums = [int(digit) for digit in num]
    #print nums
    '''
    karan:Python$ ./slideshare.py 
    [1, 2, 3, 4, 5, 5]
    [1, 6, 3, 1, 5, 2]
    
    '''
    for i in range(2, len(nums) + 1, 2):
        double = nums[len(nums) - i] * 2
        if double < 10:
            nums[len(nums) - i] = double
        else:
            nums[len(nums) - i] = sum([int(digit) for digit in str(double)])
    
    #print nums
    return sum(nums) % 10 == 0

def getFullAccountNumber(partialAccountNumber):
    for i in range(10):
        new_num = partialAccountNumber * 10 + i
        print new_num
        if isValid(new_num):
            return new_num

#print isValid(123455)
print isValid(2225)
#print '12345 is partial, full is: ' + str(getFullAccountNumber(12345)) # give me 123455

#print '11114 is partial, full is: ' + str(getFullAccountNumber(11114)) # give me 123455