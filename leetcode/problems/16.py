from typing import List
# https://leetcode.com/problems/3sum-closest/submissions/


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = 10 ** 5
        nums = sorted(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                diff_target = target - nums[i] - nums[j]
                if j == (len(nums) - 1):
                    break
                for k in range(j+1, len(nums)):
                    tmp = nums[i] + nums[j] + nums[k]
                    if tmp == target:
                        return tmp
                    if abs(target - ans) > abs(target - tmp):
                        ans = tmp
                    if diff_target < nums[k]:
                        break
        return ans
