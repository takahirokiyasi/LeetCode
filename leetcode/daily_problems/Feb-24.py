S = input()
ans = bal = 0
for i, s in enumerate(S):
    bal = bal + 1 if s == "(" else bal - 1
    if i > 0 and S[i-1:i+1] == "()":
        ans += 1 << bal
print(ans)
