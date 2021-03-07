from collections import Counter
n = int(input())
a = [int(_) for _ in input().split()]
c = Counter(a)
ans = 0
for i in range(-200, 200):
    for j in range(i+1, 201):
        ans += c[i]*c[j]*(i-j)**2
print(ans)
