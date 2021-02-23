class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        if len(s) == 1:
            return s
        for start in range(len(s) - 1):
            for end in reversed(range(start + 1, len(s) + 1)):
                if s[start: end] == s[start: end][::-1]:
                    if len(ans) < len(s[start:end]):
                        ans = s[start: end]
        return ans
