# https://atcoder.jp/contests/abc007/tasks/abc007_3
# 最短経路をキューを使って求める
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
# 1ノード降りるときにforで回せるようリスト化しておく
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 接したポイントを取り込む用のqueを定義
que = deque([])
# スタート地点をqueに加える。探索の際はqueから取り出すループを回すので最初だけ先に入れておく
que.append((sy, sx))
# スタートからスタートにかかる距離は0なのでinfを0にかえる。
d[sy][sx] = 0

# queがあるかぎり続ける
while que:
    # queから座標を取り出す。
    p = que.popleft()
    # 取り出した点がゴールなら終了
    if p[0] == gy and p[1] == gx:
        break
    #　それ以外の時は，接している点を4方向順に取得。一つずつ処理する。
    for i in range(4):
        ny = p[0] + dy[i]
        nx = p[1] + dx[i]

        # 新しく取得した座標に対しての処理
        # 迷路内に存在する座標であり，壁ではなく，まだ通ったことがなくdがinfの点なら処理する = 新しく取得した道候補の1つ
        if 0 <= ny < r and 0 <= nx < c and maze[ny][nx] != "#" and d[ny][nx] == -1:
            # 道候補をqueに加える。
            que.append((ny, nx))
            # その道候補への経路までにかかった経路をdに加える。
            d[ny][nx] = d[p[0]][p[1]] + 1

print(d[gy][gx])
