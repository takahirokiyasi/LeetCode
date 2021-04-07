s = input()
g_count = 0
p_count = 0
for tmp in s:
    if tmp == 'g':
        g_count += 1
    elif tmp == 'p':
        p_count += 1

print((g_count - p_count) // 2)
