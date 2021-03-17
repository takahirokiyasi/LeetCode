n, m = map(int, input().split())
mod = 998244353

table = [[0]*(m+1) for i in range(n+5)]
for j in range(m+1):
    table[0][j] = 1

for i in range(1, n+5):
    for j in range(m+1):
        table[i][j] = table[i-1][j]*j
        table[i][j] %= mod

ans = n*table[n][m]
for d in range(1, n):
    s = 0
    for j in range(1, m+1):
        s += table[d-1][m-j]
    ans -= s*table[n-1-d][m]*(n-d)
    ans %= mod
print(ans)
