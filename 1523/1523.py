# Accepted: 04/27/2022
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return low % 2 + high % 2 + int((high - low - low % 2 - high % 2) / 2)