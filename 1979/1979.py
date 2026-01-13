# Accepted 12/23/2022
import math


class Solution:
    def findGCD(self, nums) -> int:
        return math.gcd(min(nums), max(nums))


print(Solution().findGCD([10, 4, 2, 17]))
