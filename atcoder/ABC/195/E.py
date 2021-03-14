n = int(input())
s = str(input())
x = str(input())

dp = [[] for _ in range(n+1)]
dp[n] = [0]

for i in range(n-1, -1, -1):
    if x[i] == "T":
        for j in range(7):
            if (10*j) % 7 in dp[i+1] or (10*j+int(s[i])) % 7 in dp[i+1]:
                dp[i].append(j)
    else:
        for j in range(7):
            if (10*j) % 7 in dp[i+1] and (10*j+int(s[i])) % 7 in dp[i+1]:
                dp[i].append(j)

print("Takahashi" if 0 in dp[0] else "Aoki")
