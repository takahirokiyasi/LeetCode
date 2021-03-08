import itertools

n = int(input())
target_str = '()'

all_list = list(itertools.product(target_str, repeat=n*2))
converted_list = []
for tmp_str in all_list:
    converted_list.append(''.join(tmp_str))

ans_list = []
for tmp_str in converted_list:
    stack = []
    flag = True
    for tmp in tmp_str:
        if tmp == '(':
            stack.append('(')
        else:
            if not stack:
                flag = False
                break
            stacked_str = stack.pop()
            if stacked_str != '(':
                flag = False
                break
    else:
        if flag and len(stack) == 0:
            ans_list.append(tmp_str)

print(ans_list)
