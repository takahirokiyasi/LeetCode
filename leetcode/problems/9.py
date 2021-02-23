class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        try:
            reverse_num = int(s[::-1])
        except:
            return False
        if reverse_num == int(s):
            return True
        else:
            return False
