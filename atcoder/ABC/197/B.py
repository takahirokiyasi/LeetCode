h, w, x, y = map(int, input().split())
maps = []
for i in range(h):
    maps.append(list(input()))

x -= 1
y -= 1
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

ans = 0

if maps[x][y] == '.':
    ans += 1

for i in range(4):
    nx = x
    ny = y

    while True:
        nx += dx[i]
        ny += dy[i]

        if 0 <= nx <= h-1 and 0 <= ny <= w-1 and maps[nx][ny] == '.':
            ans += 1
        else:
            break

print(ans)
