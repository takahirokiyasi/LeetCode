N = int(input())
C = [list(map(int, input().split())) for _ in range(N)]
flag = True
A = []
B = []
for i in range(N):
    A.append(C[i][0])
amin = min(A)
for i in range(N):
    A[i] -= amin
for i in range(N):
    B.append(max(0, C[0][i] - A[0]))
for i in range(N):
    for j in range(N):
        if A[i] + B[j] != C[i][j]:
            flag = False
if flag:
    print("Yes")
    print(*A)
    print(*B)
else:
    print("No")
