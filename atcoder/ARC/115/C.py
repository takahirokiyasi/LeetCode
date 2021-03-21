N = int(input())
ans =[]
count=0
for i in range(N):
    count +=1
    if count ==1:
        ans.append(1)
    elif count%2 == 0:
        ans.append(max(ans[-1],ans[int((count//2))-1]+1))
    else:
        ans.append(ans[-1])

print(*ans)
