from decimal import Decimal
import math

x, y, r = map(Decimal, input().split())
min_x = math.ceil(x - r)
max_x = math.floor(x + r)
ans = 0
for tmp_x in range(min_x, max_x + 1):
    y_range = (r ** 2 - (tmp_x - x) ** 2).sqrt()
    ans += math.floor(y + y_range) - math.ceil(y - y_range) + 1
print(ans)
