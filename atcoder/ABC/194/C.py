N = int(input())
A = list(map(int, input().split()))

ans = 0
tmp = 0
for i in range(N):
    ans += (N - 1) * pow(A[i], 2)
    ans += -2 * A[i] * tmp
    tmp += A[i]
print(ans)
