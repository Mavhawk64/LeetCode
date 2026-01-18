# Accepted: 01/17/2026
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)  # number of vertical lines
        max_area = 0
        # ~ O(n^2)
        # for left in range(n):
        #     for right in range(left + 1, n):
        #         # Calculate the area formed by the lines at positions left and right
        #         area = min(height[left], height[right]) * (right - left)
        #         max_area = max(max_area, area)
        # Hint: Two-pointer approach
        left, right = 0, n - 1
        while left < right:
            # Calculate the area formed by the lines at positions left and right
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
