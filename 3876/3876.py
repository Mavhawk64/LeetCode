# Accepted: 09/01/2026
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odds = [i for i in nums1 if i % 2 == 1]
        return bool(len(odds) == 0 or min(odds) == min(nums1))
