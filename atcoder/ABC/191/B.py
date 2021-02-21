n, x = map(int, input().split())
a_list = []
for a in map(int, input().split()):
    if a != x:
        a_list.append(a)
print(*a_list)
