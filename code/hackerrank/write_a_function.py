'''
https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true

Task

Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

Input Format

Read , the year to test.

Output Format

The function must return a Boolean value (True/False). Output is handled by the provided code stub.
'''

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

year = int(input())
print(is_leap(year))