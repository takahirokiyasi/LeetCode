import math


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ''
        if numRows != 1:
            one_cycle_num = (numRows - 2) * 2 + 2
        else:
            one_cycle_num = 1
        s_list = list(s)
        length = len(s_list)
        zigzag = math.ceil(length / one_cycle_num)
        for j in range((one_cycle_num // 2) + 1):
            for i in range(zigzag):
                index = j + i * one_cycle_num
                try:
                    ans += s_list[index]
                except IndexError:
                    pass
                second_index = -j + (i + 1) * one_cycle_num
                if j == 0 or index == second_index:
                    continue
                try:
                    ans += s_list[second_index]
                except IndexError:
                    pass
        return ans
