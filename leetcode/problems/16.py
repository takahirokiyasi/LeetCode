from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def create_new_combination(ans: List[str], target: str) -> str:
            new_ans = []
            if not ans:
                return [i for i in target]
            if not target:
                return ans

            for a in ans:
                for t in target:
                    new_ans.append(a + t)
            return new_ans

        s_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        ans = []
        for i in digits:
            ans = create_new_combination(ans, s_dict[i])
        return ans
