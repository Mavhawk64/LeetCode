# Accepted: 04/25/2022
class Solution:
    def romanToInt(self, s: str) -> int:
        ret = 0
        if 'CM' in s:
            ret += 900
        if 'CD' in s:
            ret += 400
        if 'XC' in s:
            ret += 90
        if 'XL' in s:
            ret += 40
        if 'IX' in s:
            ret += 9
        if 'IV' in s:
            ret += 4
        s = s.replace('CM','').replace('CD','').replace('XC','').replace('XL','').replace('IX','').replace('IV','')
        return ret + s.count('M') * 1000 + s.count('D') * 500 + s.count('C') * 100 + s.count('L') * 50 + s.count('X') * 10 + s.count('V') * 5 + s.count('I')