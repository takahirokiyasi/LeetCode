n = int(input())

distance = 0
tmp_x, tmp_y = map(int, input().split())
for i in range(n-1):
    x, y = map(int, input().split())
    distance += abs(tmp_x - x) + abs(tmp_y - y)
    tmp_x = x
    tmp_y = y
print(distance)
