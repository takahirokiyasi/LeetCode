def divisor(n):
    i = 1
    table = []
    odd = 0
    even = 0
    while i * i <= n:
        if n % i == 0:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
            table.append(n//i)
            if (n // i) % 2 == 0:
                even += 1
            else:
                odd += 1
        i += 1
    if odd == even:
        return 'Same'
    elif odd > even:
        return 'Odd'
    else:
        return 'Even'


T = int(input())
for i in range(T):
    print(divisor(int(input())))
