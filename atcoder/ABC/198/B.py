N = int(input())
while N % 10 == 0:
    N /= 10

N = int(N)
if str(N)[::-1] == str(N):
    print("Yes")
else:
    print("No")
