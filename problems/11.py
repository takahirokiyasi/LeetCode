a_list = list(map(int, input().split()))
max_val, start, end = 0, 0, len(a_list)-1

while start < end:
    if a_list[start] < a_list[end]:
        max_val = max(max_val, a_list[start]*(end-start))
        start += 1
    else:
        max_val = max(max_val, a_list[end]*(end-start))
        end -= 1
print(max_val)
