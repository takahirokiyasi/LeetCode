n = int(input())
li = set()
for a in range(2, 10**5+1):
    b = 2
    while a**b <= n:
        li.add(a**b)
        b += 1

print(n-len(li))
