# https://leetcode.com/problems/container-with-most-water/
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea, start, end = 0, 0, len(height) - 1

        while start < end:
            a = end - start
            if height[start] < height[end]:
                maxArea = max(maxArea, a * height[start])
                start += 1
            else:
                maxArea = max(maxArea, a * height[end])
                end -= 1

        return maxArea
