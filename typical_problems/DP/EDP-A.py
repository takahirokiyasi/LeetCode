n = int(input())
h = list(map(int, input().split()))

h_memo = [-1] * len(h)
h_memo[0] = 0
h_memo[1] = abs(h[0] - h[1])
for i in range(2, len(h)):
    a = h_memo[i-2] + abs(h[i] - h[i-2])
    b = h_memo[i-1] + abs(h[i] - h[i-1])
    h_memo[i] = min(a, b)
print(h_memo[-1])
