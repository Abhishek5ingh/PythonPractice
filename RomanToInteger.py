# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        val = []
        for j in s:
            val.append(roman[j])
        for i in range(len(s) - 1):
            if val[i] < val[i+1]:
                val[i] = -val[i]
        return sum(val)
