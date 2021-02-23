class Solution:
    def romanToInt(self, s: str) -> int:
        s_list = list(s)
        roman_list = {'I': 1, 'V': 5, 'X': 10,
                      'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        before_val = 0
        stock_val = 0
        for tmp in reversed(s_list):
            val = roman_list[tmp]
            if before_val <= val:
                ans += (val - stock_val)
                stock_val = 0
            else:
                stock_val += val
            before_val = val

        ans -= stock_val

        return ans
