# https://atcoder.jp/contests/abc197/tasks/abc197_c

# bit全探索
# https://qiita.com/gogotealove/items/11f9e83218926211083a

N = int(input())
A = list(map(int, input().split()))
ans = float('inf')

# Aの各間をORにするかXORするかなのでN-1　XORしたときbitが1とする
for i in range(2**(N-1)):
    xored = 0
    ored = 0
    for j in range(N-1):
        # 今までORされてきたもの
        ored |= A[j]
        # 順に一つずつビットシフトしていき1の時はそれが選ばれているとする
        if (i >> j) & 1:
            xored ^= ored
            ored = 0
    ored |= A[N-1]
    xored ^= ored
    ans = min(ans, xored)

print(ans)
