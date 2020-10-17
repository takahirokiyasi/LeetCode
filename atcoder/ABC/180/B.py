from math import sqrt
n = int(input())
x = list(map(lambda x: abs(int(x)), input().split()))
print(sum(x))
print(sqrt(sum([i**2 for i in x])))
print(max(x))
