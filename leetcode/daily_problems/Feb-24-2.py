# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3651/
S = input()
stack = []
tmp = 0
for i, s in enumerate(S):
    if s == '(':
        stack.append('(')
    else:
        while stack[-1] != '(':
            tmp += stack[-1]
            stack.pop()
        stack[-1] = tmp * 2 if tmp else 1
        tmp = 0
print(sum(stack))
