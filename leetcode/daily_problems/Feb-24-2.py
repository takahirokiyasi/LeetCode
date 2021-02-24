# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3651/
S = input()
crr, stack = 0, []
for pos in range(len(S)):
    if S[pos] == '(':
        stack.append('(')
    else:
        while stack[-1] != '(':
            crr += stack[-1]
            stack.pop()
        stack[-1] = crr * 2 if crr else 1
        crr = 0
print(sum(stack))
