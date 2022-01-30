s = list(input())
a, b = map(int, input().split())
a_st = s[a-1]
b_st = s[b-1]
s[a-1] = b_st
s[b-1] = a_st

print(''.join(s))