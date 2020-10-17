x, y, a, b = map(int, input().split())
ans = 0
while (a - 1) * x < b and x * a < y:
    ans += 1
    x *= a

ans += (y - x - 1)//b
print(ans)
