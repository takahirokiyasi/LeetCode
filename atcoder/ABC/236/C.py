n, m = map(int, input().split())
s_list = list(input().split())
t_list = list(input().split())
tmp_t = t_list.pop(0)
for s in s_list:
    if s == tmp_t:
        print('Yes')
        try:
            tmp_t = t_list.pop(0)
        except Exception:
            exit()
    else:
        print('No')