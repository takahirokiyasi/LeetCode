# https://leetcode.com/problems/longest-common-prefix/
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        common_str = strs[0]
        for i in range(1, len(strs)):
            target = strs[i]
            while True:
                if common_str == "":
                    return ""
                if target[:len(common_str)] == common_str:
                    common_str = target[:len(common_str)]
                    break
                common_str = common_str[:-1]
        return common_str
