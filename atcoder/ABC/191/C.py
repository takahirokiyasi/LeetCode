H, W = map(int, input().split())
grid = [input() for _ in range(H)]

ans = 0
for h in range(H-1):
    for w in range(W-1):
        count = 0
        for i in range(h, h+2):
            for j in range(w, w+2):
                if grid[i][j] == '#':
                    count += 1

        if count == 1 or count == 3:
            ans += 1
