num_list = list(map(int, input().split()))
split_num = sum(num_list)/2

for i in num_list:
    if split_num == i:
        print('Yes')
        exit()
for index_j, j in enumerate(num_list):
    for index_l, l in enumerate(num_list):
        if index_j != index_l:
            if split_num == j+l:
                print('Yes')
                exit()

print('No')
