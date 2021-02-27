# https://leetcode.com/problems/3sum-closest/
# しゃくとり法は条件を満たす区間を全列挙する手法
from typing import List


def solution(nums: List[int], target: int):

    nums.sort()
    n = len(nums)
    closest_diff = float('Inf')
    out = []
    for i in range(n-2):
        l = i+1
        r = n-1
        while l < r:
            temp_list = [nums[i], nums[l], nums[r]]
            temp_sum = sum(temp_list)
            curr_diff = temp_sum-target
            if abs(curr_diff) < closest_diff:
                out = temp_list
                closest_diff = abs(curr_diff)
            if curr_diff == 0:
                return sum(out)
            elif curr_diff > 0:
                r -= 1
            elif curr_diff < 0:
                l += 1
    return sum(out)


nums = list(map(int, input().split()))
target = int(input())
print(solution(nums, target))
