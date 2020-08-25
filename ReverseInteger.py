# Given a 32-bit signed integer, reverse digits of an integer.

class Solution:
    def reverse(self, x: int) -> int:
        a = ''
        if '-' in str(x):
            a = str(x)[1:]
            b = '-' + a[::-1]
        else: 
            a = str(x)
            b = a[::-1]
        if int(b) > pow(2,31) or int(b) < -pow(2,31):
            return 0
        else:
            return int(b)
        return 
            
