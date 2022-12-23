# Accepted: 04/25/2022
class Solution:
    def intToRoman(self, num: int) -> str:
        ret = ''
        ret += int(num / 1000) * 'M'
        num %= 1000
        if num - 900 >= 0:
            ret += 'CM'
            num -= 900
        if 400 <= num < 500:
            ret += 'CD'
            num -= 400
        ret += int(num / 500) * 'D'
        num %= 500
        ret += int(num / 100) * 'C'
        num %= 100
        if num - 90 >= 0:
            ret += 'XC'
            num -= 90
        if 40 <= num < 50:
            ret += 'XL'
            num -= 40
        ret += int(num / 50) * 'L'
        num %= 50
        ret += int(num / 10) * 'X'
        num %= 10
        if num == 9:
            return ret + 'IX'
        if num == 4:
            return ret + 'IV'
        ret += int(num / 5) * 'V'
        num %= 5
        return ret + num * 'I'