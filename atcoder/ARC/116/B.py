n = int(input())
a = list(map(int, input().split()))
MOD = 998244353

a.sort()
ans = (a[-1]*a[-1]) % MOD
t = a[-1] % MOD

for i in range(n-2, -1, -1):
    tmp = a[i] % MOD
    ans += (tmp*t) % MOD
    ans += (tmp*tmp) % MOD
    t = (2*t + tmp) % MOD
