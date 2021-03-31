n = int(input())
x_list = list(map(int, input().split()))
x_list.sort(reverse=True)
print(x_list)


def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return sorted(table)


divisors_set = set()
for x in x_list:
    tmp = divisor(x)
    common = set(tmp[2:]) & divisors_set
    if len(common) > 0:
        divisors_set.add(list(common)[0])
    else:
        divisors_set.add(tmp[1])
ans = 1
for i in divisors_set:
    ans *= i

print(ans)
