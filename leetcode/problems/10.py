class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        string = list(s)
        string.reverse()
        rpat = []
        i = len(p)-1
        while i >= 0:
            if p[i] == '*':
                rpat.append('*'+p[i-1])
                i -= 1
            else:
                rpat.append(p[i])
            i -= 1
        if len(string) == 0 and len(rpat) == 0:
            return True
        if len(rpat) == 0:
            return False
        if p[0] == '*':
            return False

        dp = [[0]*(len(string)+1) for _ in range(1+len(rpat))]
        dp[0][0] = 1
        for i in range(1, len(rpat)+1):

            if rpat[i-1] == '.':
                for j in range(1, len(string)+1):
                    dp[i][j] = dp[i-1][j-1]
            elif rpat[i-1][0] != '*':
                for j in range(1, len(string)+1):
                    if rpat[i-1] == string[j-1] and dp[i-1][j-1]:
                        dp[i][j] = 1
            else:
                if rpat[i-1][1] == '.':
                    dp[i][0] = dp[i-1][0]
                    for j in range(1, len(string)+1):
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                else:
                    dp[i][0] = dp[i-1][0]
                    for j in range(1, len(string)+1):
                        if dp[i-1][j] or (string[j-1] == rpat[i-1][1] and (dp[i-1][j-1] or dp[i][j-1])):
                            dp[i][j] = 1
        print(dp)
        return dp[-1][-1]
