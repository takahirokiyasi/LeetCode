from collections import deque

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
maze = [list(input()) for i in range(r)]

sy -= 1
sx -= 1
gy -= 1
gx -= 1

d = [[-1] * c for i in range(r)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

que = deque([])
que.append((sy, sx))

d[sy][sx] = 0

while que:
    p = que.popleft()
    if p[0] == gy and p[1] == gx:
        break
    for i in range(4):
        ny = p[0] + dy[i]
        nx = p[1] + dx[i]

        if 0 <= ny < r and 0 <= nx < c and maze[ny][nx] != "#" and d[ny][nx] == -1:
            que.append((ny, nx))
            d[ny][nx] = d[p[0]][p[1]] + 1
print(d[gy][gx])
