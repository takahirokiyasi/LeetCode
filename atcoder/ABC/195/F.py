primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
          31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
A, B = map(int, input().split())
dp = [0] * (1 << 20)
dp[0] = 1
for x in range(A, B + 1):
    bit = 0
    for i in range(20):
        if x % primes[i] == 0:
            bit |= 1 << i
    for i in range(1 << 20):
        if (i & bit) == 0:
            dp[i | bit] += dp[i]
print(sum(dp))
