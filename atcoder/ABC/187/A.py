A, B = input().split()
A = list(map(lambda x: int(x), list(A)))
B = list(map(lambda x: int(x), list(B)))
sum(A)
sum(B)
print(max(sum(A), sum(B)))