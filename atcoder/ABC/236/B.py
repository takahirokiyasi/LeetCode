n = int(input())
a_list = list(map(int, input().split()))
print(((n+1)*n)*2 - sum(a_list))