# https://atcoder.jp/contests/abc197/tasks/abc197_c

N = int(input())
A = list(map(int, input().split()))
ans = float('inf')

for i in range(2**(N-1)):
    xored = 0
    ored = 0
    for j in range(N-1):
        ored |= A[j]
        if (i >> j) & 1:
            xored ^= ored
            ored = 0
    ored |= A[N-1]
    xored ^= ored
    ans = min(ans, xored)

print(ans)
