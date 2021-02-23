class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        substring = []
        for i in list(s):
            if i in substring:
                j = substring.index(i)
                substring = substring[j+1:]

            substring.append(i)
            if ans < len(substring):
                ans = len(substring)
        return ans
