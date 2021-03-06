n = int(input())
a_list = []
b_list = []
for i in range(n):
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)
a_min = min(a_list)
b_min = min(b_list)
if a_list.index(a_min) == b_list.index(b_min):
    a_second_min = sorted(a_list)[1]
    b_second_min = sorted(b_list)[1]
    print(min(min(max(a_second_min, b_min), max(a_min, b_second_min)), a_min + b_min))
else:
    print(max(a_min, b_min))
