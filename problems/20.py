stack = []
s_list = list(input())
target_dict = {'[': ']',  '(': ')', '{': '}'}
for s in s_list:
    if len(stack) > 0 and target_dict.get(stack[len(stack)-1]) == s:
        stack.pop()
    else:
        stack.append(s)
print('True') if len(stack) == 0 else print('False')
