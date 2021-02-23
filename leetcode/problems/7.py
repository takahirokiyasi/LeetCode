class Solution:
    def reverse(self, x: int) -> int:
        limit = 2 ** 31
        isNegative = x < 0
        x = int(str(abs(x))[::-1])
        if x < -limit or x > limit - 1:
            return 0
        if isNegative:
            x = -x
        return x
