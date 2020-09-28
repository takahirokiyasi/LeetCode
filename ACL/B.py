a, b, c, d = map(int, input().split())
min_num = a if a > c else c
max_num = d if b > d else b

print('Yes') if max_num >= min_num else print('No')
