N = int(input())
if N == 0:
    print('Yes')
    exit()
while N % 10 == 0:
    N /= 10

N = str(int(N))
if N[::-1] == N:
    print("Yes")
else:
    print("No")
