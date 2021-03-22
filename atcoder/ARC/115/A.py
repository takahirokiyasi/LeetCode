N, M = map(int, input().split())
odd = 0
even = 0
for i in range(N):
    if input().count('1') % 2 == 0:
        even += 1
    else:
        odd += 1
ans = even * odd
print(ans)
