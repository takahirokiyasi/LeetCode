n, k = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(n)]


v_list = []
min_val = 0
for row in matrix:
    for i, v in enumerate(row):
        if min_val <= v:
            v_list.append(len(row) - i)
            min_val = v
            break
    else:
        ans = 0
        break


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


ans =
for i in v_list:

print(ans % ((10 ** 9) + 7))
