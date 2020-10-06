# https://atcoder.jp/contests/agc033/tasks/agc033_a
# 多点スタートな最短経路問題

from collections import deque

H, W = map(int, input().split())
grid = [input() for i in range(H)]

# 初期の黒('#')の位置からの距離
dist = [[-1]*W for _ in range(H)]


# '#'の位置をキューに追加（＝今回はこれが複数あるので、複数スタートとなる）
black_cells = deque()
for h in range(H):
    for w in range(W):
        if grid[h][w] == '#':
            black_cells.append((h, w))
            dist[h][w] = 0


def bfs(black_cells, dist):
    """
    BFSを用いて、全マス目を黒くする回数を求める

    Args:
        black_cells: 「開始時の黒マス」の座標が入ったキュー（複数座標あり）
        dist: 「開始時の黒マス」からの距離の入ったリスト  [[-1, -1, 0], ...]
        　　　　　　　　　　　　　　　　　　　　　　　　（白マスの初期値は0）

    Returns:
        g: 操作を繰り返した数
    """
    d = 0
    while black_cells:
        # キューとして使うのでpop()ではなくpopleft()
        h, w = black_cells.popleft()
        d = dist[h][w]
        for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            new_h = h + dy
            new_w = w + dx
            if new_h < 0 or H <= new_h or new_w < 0 or W <= new_w:
                continue
            if dist[new_h][new_w] == -1:  # セルが白('.')であるのと同義
                dist[new_h][new_w] = d+1
                black_cells.append((new_h, new_w))
    return d


d = bfs(black_cells, dist)
print(d)
