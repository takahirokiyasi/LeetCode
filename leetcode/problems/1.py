from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        differenceMap = dict()
        for i, num in enumerate(nums):
            diff = target - num
            if diff in differenceMap:
                ans = [differenceMap[diff], i]
                break
            else:
                differenceMap[num] = i
        return ans
