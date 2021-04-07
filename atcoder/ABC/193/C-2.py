N = int(input())
res = set()
for i in range(2, int(N**0.5)+1):
    tmp = 2
    while i ** tmp <= N:
        res.add(i ** tmp)
        tmp += 1

print(N - len(res))
