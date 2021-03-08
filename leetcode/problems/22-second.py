from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = list()

        def backtrack(count: int = 0, solution: List[str] = []) -> None:
            if len(solution) == 2 * n:
                if count == 0:
                    ans.append("".join(solution))
                return

            if count > 0:
                solution.append(")")
                backtrack(count - 1, solution)
                solution.pop()

            solution.append("(")
            backtrack(count + 1, solution)
            solution.pop()

        backtrack()
        return ans
